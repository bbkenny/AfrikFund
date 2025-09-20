
# agents/blockchain_agent.py
import time

def record_debt(details):
    """
    Simulates recording debt details on Solana blockchain.
    Returns a mock transaction ID.
    """
    # Simulate processing time
    time.sleep(1)
    
    # Generate a realistic-looking mock Solana transaction ID
    mock_txid = f"5gn1W{int(time.time())}W{sorted(details.items())[0][1][:8]}"
    return mock_txid.upper().replace(" ", "")
