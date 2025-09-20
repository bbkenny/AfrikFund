# agents/nft_agent.py
import time
import random

def mint_nft(txid, employee_email):
    """
    Simulates minting a Proof of Debt NFT via Crossmint.
    Returns a mock NFT ID.
    """
    # Simulate processing time
    time.sleep(1)
    
    # Generate a realistic-looking mock Crossmint NFT ID
    email_prefix = employee_email.split('@')[0]
    mock_nft_id = f"crossmint:{email_prefix}:{txid[:8]}-{random.randint(1000,9999)}"
    return mock_nft_id.lower()
