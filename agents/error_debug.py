import json
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Confirmed
# Use the high-performance `solders` library for core types
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.transaction import Transaction
from solders.instruction import Instruction

# --- Configuration ---
# We will connect to the Solana Devnet for testing.
DEVNET_URL = "https://api.devnet.solana.com"
# The public key of the official Solana Memo Program
MEMO_PROGRAM_ID = Pubkey.from_string("MemoSq4gqABAXKb96qnH8TysNcVnuvMvKdkdcMAwn9B")

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
        print(f"🔑 Generated a temporary payer wallet: {payer.pubkey()}")

        # 3. --- Airdrop SOL for Transaction Fees ---
        print("💸 Requesting a SOL airdrop to pay for fees...")
        airdrop_response = solana_client.request_airdrop(payer.pubkey(), 2 * 10**9) # 2 SOL
        airdrop_signature = airdrop_response.value
        
        # FIX: Get latest blockhash and use its context to confirm the transaction.
        latest_blockhash_response = solana_client.get_latest_blockhash()
        solana_client.confirm_transaction(
            airdrop_signature,
            last_valid_block_height=latest_blockhash_response.value.last_valid_block_height
        )
        print(f"✅ Airdrop successful. TXID: {airdrop_signature}")

        # 4. --- Format the Debt Details for the Memo ---
        memo_text = json.dumps(details)
        print(f"📝 Preparing memo: {memo_text}")
        
        if len(memo_text.encode('utf-8')) > 566: # Solana memo has a size limit
            return "Error: Debt details are too long for a Solana memo."

        # 5. --- Create the Memo Instruction ---
        # An "instruction" tells the blockchain what to do.
        instruction = Instruction(
            program_id=MEMO_PROGRAM_ID,
            data=memo_text.encode('utf-8'),
            accounts=[] # The memo program doesn't require any accounts.
        )
        
        # 6. --- Build the Transaction ---
        # FIX: Reuse the blockhash we already fetched.
        latest_blockhash = latest_blockhash_response.value.blockhash
        
        transaction = Transaction.new_signed_with_payer(
            instructions=[instruction],
            payer=payer.pubkey(),
            signing_keypairs=[payer],
            recent_blockhash=latest_blockhash
        )

        # 7. --- Sign and Send the Transaction ---
        print("🚀 Sending transaction to the blockchain...")
        
        send_tx_response = solana_client.send_transaction(
            transaction,
            opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed)
        )
        
        txid = send_tx_response.value
        print(f"✅ Transaction sent successfully!")
        print(f"🔗 Transaction ID (txid): {txid}")

        return str(txid)

    except Exception as e:
        # FIX: Ensure the returned error message starts with "Error:"
        error_message = f"Error: An error occurred: {e}"
        print(f"❌ {error_message}")
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

    if transaction_id and "Error" not in transaction_id:
        print("\n--- ✅ Proof of Debt Recorded Successfully ---")
        print(f"Transaction ID: {transaction_id}")
        print(f"View it on the Solana Explorer: https://explorer.solana.com/tx/{transaction_id}?cluster=devnet")
    else:
        print("\n--- ❌ Failed to Record Proof of Debt ---")
        print(f"Reason: {transaction_id}")

