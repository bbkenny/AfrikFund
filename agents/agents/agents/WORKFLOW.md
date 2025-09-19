# PayGuard Workflow

1.  **Input:** User provides employer name, employee email/wallet, debt amount, due date.
2.  **Blockchain Agent:**
    - Function: `record_debt(details)`
    - Connects to Solana Devnet.
    - Creates a transaction with the debt details in a memo.
    - Returns a Transaction ID (txid).
3.  **NFT Agent:**
    - Function: `mint_nft(txid, employee_email)`
    - Uses the Crossmint Staging API.
    - Mints an NFT to the employee's email with the txid in the description.
    - Returns an NFT ID.
4.  **App (Streamlit):**
    - Displays the TXID and NFT ID as proof to the user.
