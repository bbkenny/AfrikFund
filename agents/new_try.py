import json
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.pubkey import Pubkey as PublicKey
from solders.transaction import Transaction
from solders.instruction import Instruction
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Confirmed

# --- Configuration ---
DEVNET_URL = "https://api.devnet.solana.com"
# --- FIX IS HERE ---
# We now use PublicKey.from_string() to correctly parse the Base58 address.
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
        airdrop_signature = airdrop_response.value
        solana_client.confirm_transaction(airdrop_signature)
        print(f"✅ Airdrop successful. TXID: {airdrop_signature}")

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

        # 7. --- Sign and Send the Transaction ---
        print("🚀 Sending transaction to the blockchain...")
        
        send_tx_response = solana_client.send_transaction(
            transaction,
            payer,
            opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed)
        )
        
        txid = send_tx_response.value
        print(f"✅ Transaction sent successfully!")
        print(f"🔗 Transaction ID (txid): {txid}")

        return str(txid)

    except Exception as e:
        error_message = f"An error occurred: {e}"
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

    if "Error" not in transaction_id and transaction_id is not None:
        print("\n--- ✅ Proof of Debt Recorded Successfully ---")
        print(f"Transaction ID: {transaction_id}")
        print(f"View it on the Solana Explorer: https://explorer.solana.com/tx/{transaction_id}?cluster=devnet")
    else:
        print("\n--- ❌ Failed to Record Proof of Debt ---")
        print(f"Reason: {transaction_id}")

