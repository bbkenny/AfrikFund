import json
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.pubkey import Pubkey as PublicKey
from solders.transaction import Transaction
from solders.instruction import Instruction
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Confirmed

# --- Configuration ---
# We will connect to the Solana Devnet for testing.
DEVNET_URL = "https://api.devnet.solana.com"
# The public key of the official Solana Memo Program
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
        # In a real app, you would load a securely stored private key for your service's wallet.
        # For this example, we'll generate a new one each time.
        # **IMPORTANT**: This new account needs SOL to pay for transactions.
        payer = Keypair()
        payer_public_key = payer.pubkey()
        print(f"🔑 Generated a temporary payer wallet: {payer_public_key}")

        # 3. --- Airdrop SOL for Transaction Fees ---
        # We need to fund this new wallet to pay for the transaction fee.
        print("💸 Requesting a SOL airdrop to pay for fees...")
        airdrop_response = solana_client.request_airdrop(payer_public_key, 2 * 10**9) # 2 SOL
        # Use .value to get the signature from the response object
        airdrop_signature = airdrop_response.value

        # FIX: Get latest blockhash and use its context to confirm the transaction.
        latest_blockhash_response = solana_client.get_latest_blockhash()
        solana_client.confirm_transaction(
            airdrop_signature,
            last_valid_block_height=latest_blockhash_response.value.last_valid_block_height
        )
        print(f"✅ Airdrop successful. TXID: {airdrop_signature}")



        # 4. --- Format the Debt Details for the Memo ---
        # We convert the dictionary into a JSON string to store it as a single piece of text.
        # This makes it structured and easy to read later.
        memo_text = json.dumps(details)
        print(f"📝 Preparing memo: {memo_text}")
        
        if len(memo_text.encode('utf-8')) > 566: # Solana memo has a size limit
            return "Error: Debt details are too long for a Solana memo."

        # 5. --- Build the Transaction ---
        # A transaction is a container for one or more instructions.
        transaction = Transaction()

        # 6. --- Create the Memo Instruction ---
        # An "instruction" tells the blockchain what to do. Here, we're telling
        # the Memo Program to process our text data.
        instruction = Instruction(
            program_id=MEMO_PROGRAM_ID,
            data=memo_text.encode('utf-8'),
            keys=[] # The memo program doesn't require any accounts to be passed in `keys`.
        )
        transaction.add(instruction)

        # 7. --- Sign and Send the Transaction ---
        print("🚀 Sending transaction to the blockchain...")
        
        # We sign the transaction with our payer's keypair to authorize the payment.
        # Then, we send it to the Solana network.
        result = solana_client.send_transaction(
            transaction,
            payer,
            opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed)
        )
        
        txid = result['result']
        print(f"✅ Transaction sent successfully!")
        print(f"🔗 Transaction ID (txid): {txid}")

        return str(txid)

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(f"❌ {error_message}")
        return error_message

# --- Example Usage ---
if __name__ == '__main__':
    # This block will only run when you execute this script directly
    # It won't run when you import the function into your Streamlit app.
    
    print("--- Running a test for record_debt() ---")

    # 1. Input: Define the debt details
    debt_details = {
        "employer_name": "Innovate Corp",
        "employee_wallet": "7iY1gV1cbkggftQS5G5YgSH8EH4n2U1f1a5fGzS6j4qP", # Example wallet address
        "debt_amount": "5000 USD",
        "due_date": "2025-09-15"
    }

    # 2. Blockchain Agent: Call the function
    transaction_id = record_debt(debt_details)

    # 3. App: Display the result
    if "Error" not in transaction_id:
        print("\n--- ✅ Proof of Debt Recorded Successfully ---")
        print(f"Transaction ID: {transaction_id}")
        print(f"View it on the Solana Explorer: https://explorer.solana.com/tx/{transaction_id}?cluster=devnet")
    else:
        print("\n--- ❌ Failed to Record Proof of Debt ---")
        print(f"Reason: {transaction_id}")
