import json
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.pubkey import Pubkey as PublicKey
from solders.transaction import Transaction
from solders.instruction import Instruction
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Confirmed
import time
from solders.rpc.responses import RequestAirdropResp, SendTransactionResp

# --- Configuration ---
DEVNET_URL = "https://api.devnet.solana.com"
MEMO_PROGRAM_ID = PublicKey.from_string("MemoSq4gqABAXKb96qnH8TysNcVnuvMvKdkdcMAwn9B")

def record_debt(details: dict) -> str:
    """
    Connects to the Solana Devnet and records debt details in a transaction memo.

    Args:
        details (dict): A dictionary containing debt information.
                        Expected keys: 'employer_name', 'employee_wallet',
                                       'debt_amount', 'due_date'.

    Returns:
        str: The transaction ID (signature) of the confirmed transaction on the Devnet.
             Returns an error message string on failure.
    """
    try:
        # 1. --- Establish Connection to Solana Devnet ---
        print("🔌 Connecting to Solana Devnet...")
        solana_client = Client(DEVNET_URL)
        if not solana_client.is_connected():
            return "Error: Could not connect to the Solana Devnet."
        print("✅ Connection successful.")

        # 2. --- Create a Payer Account ---
        payer = Keypair()
        payer_public_key = payer.pubkey()
        print(f"🔑 Generated a temporary payer wallet: {payer_public_key}")

        # 3. --- Airdrop SOL for Transaction Fees ---
        print("💸 Requesting a SOL airdrop to pay for fees...")
        airdrop_response = solana_client.request_airdrop(payer_public_key, 2 * 10**9) # 2 SOL
        
        # Check if airdrop was successful
        if hasattr(airdrop_response, 'value') and airdrop_response.value:
            airdrop_signature = airdrop_response.value
            print(f"✅ Airdrop requested. TXID: {airdrop_signature}")
            
            # Wait for airdrop confirmation
            print("⏳ Waiting for airdrop to be confirmed...")
            time.sleep(10)  # Wait longer for airdrop to be processed
            
            # Verify balance
            balance_response = solana_client.get_balance(payer_public_key)
            if hasattr(balance_response, 'value') and balance_response.value:
                balance = balance_response.value
                print(f"💰 Current balance: {balance} lamports")
                if balance == 0:
                    return "Error: Airdrop failed - balance is still zero"
        else:
            return "Error: Airdrop request failed"

        # 4. --- Format the Debt Details for the Memo ---
        memo_text = json.dumps(details)
        print(f"📝 Preparing memo: {memo_text}")
        
        if len(memo_text.encode('utf-8')) > 566: # Solana memo has a size limit
            return "Error: Debt details are too long for a Solana memo."

        # 5. --- Build the Transaction ---
        transaction = Transaction()

        # 6. --- Create the Memo Instruction ---
        instruction = Instruction(
            program_id=MEMO_PROGRAM_ID,
            data=memo_text.encode('utf-8'),
            keys=[]
        )
        transaction.add(instruction)

        # 7. --- Get recent blockhash ---
        blockhash_response = solana_client.get_latest_blockhash()
        if hasattr(blockhash_response, 'value') and blockhash_response.value:
            recent_blockhash = blockhash_response.value.blockhash
            transaction.recent_blockhash = recent_blockhash
            transaction.fee_payer = payer_public_key
        else:
            return "Error: Failed to get recent blockhash"

        # 8. --- Sign and Send the Transaction ---
        print("🚀 Sending transaction to the blockchain...")
        
        # Sign the transaction
        transaction.sign([payer])
        
        # Send the transaction
        send_tx_response = solana_client.send_transaction(
            transaction,
            payer,
            opts=TxOpts(skip_preflight=False, preflight_commitment=Confirmed)
        )
        
        # Check if transaction was sent successfully
        if hasattr(send_tx_response, 'value') and send_tx_response.value:
            txid = send_tx_response.value
            print(f"✅ Transaction sent successfully!")
            print(f"🔗 Transaction ID (txid): {txid}")
            
            # Wait for confirmation
            print("⏳ Waiting for transaction confirmation...")
            time.sleep(5)  # Wait for confirmation
            
            # Check transaction status
            confirm_response = solana_client.get_transaction(txid, commitment="confirmed")
            if hasattr(confirm_response, 'value') and confirm_response.value:
                print("✅ Transaction confirmed on chain!")
                return str(txid)
            else:
                return "Error: Transaction confirmation failed"
        else:
            return "Error: Failed to send transaction"

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(f"❌ {error_message}")
        import traceback
        traceback.print_exc()
        return error_message

# --- Example Usage ---
if __name__ == '__main__':
    print("--- Running a test for record_debt() ---")

    debt_details = {
        "employer_name": "Innovate Corp",
        "employee_wallet": "7iY1gV1cbkggftQS5G5YgSH8EH4n2U1f1a5fGzS6j4qP",
        "debt_amount": "5000 USD",
        "due_date": "2025-09-15"
    }

    transaction_id = record_debt(debt_details)

    if transaction_id and not transaction_id.startswith("Error") and not transaction_id.startswith("An error occurred"):
        print("\n--- ✅ Proof of Debt Recorded Successfully ---")
        print(f"Transaction ID: {transaction_id}")
        print(f"View it on the Solana Explorer: https://explorer.solana.com/tx/{transaction_id}?cluster=devnet")
    else:
        print("\n--- ❌ Failed to Record Proof of Debt ---")
        print(f"Reason: {transaction_id}")