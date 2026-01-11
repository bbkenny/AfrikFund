# import json
# from solana.rpc.api import Client
# from solders.keypair import Keypair
# from solders.pubkey import Pubkey
# from solders.transaction import Transaction
# from solders.instruction import Instruction
# from solana.rpc.types import TxOpts
# import base58
# import os
# from datetime import datetime
# import requests


# class PayGuardBlockchainAgent:
#     def __init__(self):
#         load_dotenv()
#         self.solana_client = Client("https://api.devnet.solana.com")
#         self.memo_program_id = Pubkey.from_string("MemoSq4gqABAXKb96qnH8TysNcVnuvMvKdkdcMAwn9B")
#         self.company_wallet = self._load_wallet()
    
#     def _load_wallet(self):
#         private_key = os.getenv('COMPANY_WALLET_PRIVATE_KEY')
#         if not private_key:
#             raise ValueError("COMPANY_WALLET_PRIVATE_KEY not found in environment variables")
#         print(private_key)   
#         return Keypair.from_bytes(base58.b58decode(private_key))
    
#     def record_debt_on_chain(self, debt_details):
#         try:
#             metadata = {
#                 **debt_details,
#                 "recorded_at": datetime.utcnow().isoformat(),
#                 "type": "proof_of_debt",
#                 "version": "1.0"
#             }
            
#             memo_text = json.dumps(metadata)
            
#             # Get recent blockhash
#             latest_blockhash = self.solana_client.get_latest_blockhash().value.blockhash
            
#             instruction = Instruction(
#                 program_id=self.memo_program_id,
#                 data=memo_text.encode('utf-8'),
#                 accounts=[]
#             )
            
#             transaction = Transaction.new_signed_with_payer(
#                 instructions=[instruction],
#                 payer=self.company_wallet.pubkey(),
#                 signing_keypairs=[self.company_wallet],
#                 recent_blockhash=latest_blockhash
#             )
            
#             response = self.solana_client.send_transaction(
#                 transaction,
#                 opts=TxOpts(skip_preflight=False)
#             )
            
#             txid = str(response.value)
#             return {
#                 "success": True,
#                 "transaction_id": txid,
#                 "explorer_url": f"https://explorer.solana.com/tx/{txid}?cluster=devnet",
#                 "metadata": metadata
#             }
            
#         except Exception as e:
#             return {"success": False, "error": str(e)}
    
#     def mint_proof_of_debt_nft(self, debt_metadata, employee_wallet):
#         try:
#             nft_metadata = {
#                 "name": f"Proof of Debt - {debt_metadata['employer_name']}",
#                 "description": f"Verified debt acknowledgment for {debt_metadata['employee_name']}",
#                 "image": "https://ipfs.io/ipfs/QmX6z6Q7R8RZ5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z",
#                 "attributes": [
#                     {"trait_type": "Debt Amount", "value": debt_metadata['debt_amount']},
#                     {"trait_type": "Due Date", "value": debt_metadata['due_date']},
#                     {"trait_type": "Employer", "value": debt_metadata['employer_name']},
#                     {"trait_type": "Employee", "value": debt_metadata['employee_name']},
#                     {"trait_type": "Recorded On", "value": debt_metadata['recorded_at']}
#                 ]
#             }
            
#             headers = {
#                 "X-CLIENT-SECRET": os.getenv('CROSSMINT_API_KEY'),
#                 "Content-Type": "application/json"
#             }
            
#             payload = {
#                 "recipient": f"solana:{employee_wallet}",
#                 "metadata": nft_metadata,
#                 "reuploadLinkedFiles": True
#             }
            
#             collection_id = os.getenv('CROSSMINT_COLLECTION_ID')
#             response = requests.post(
#                 f"https://www.crossmint.com/api/2022-06-09/collections/{collection_id}/nfts",
#                 headers=headers,
#                 json=payload
#             )
            
#             if response.status_code == 200:
#                 return {
#                     "success": True,
#                     "nft_id": response.json().get('id'),
#                     "nft_metadata": nft_metadata
#                 }
#             else:
#                 return {"success": False, "error": response.text}
                
#         except Exception as e:
#             return {"success": False, "error": str(e)}

import json
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.transaction import Transaction
from solders.instruction import Instruction
from solana.rpc.types import TxOpts
import base58
import os
from datetime import datetime
import requests
from dotenv import load_dotenv

class PayGuardBlockchainAgent:
    def __init__(self):
        load_dotenv()
        self.solana_client = Client("https://api.devnet.solana.com")
        self.memo_program_id = Pubkey.from_string("Memo1UhkJRfHyvLMcVucJwxXeuD728EqVDDwQDxFMNo")  # Use devnet memo
        self.company_wallet = self._load_wallet()
    
    def _load_wallet(self):
        private_key = os.getenv('COMPANY_WALLET_PRIVATE_KEY')
        if not private_key:
            raise ValueError("COMPANY_WALLET_PRIVATE_KEY not found in environment variables")
        print(f"Private key loaded: {private_key[:10]}...")   
        return Keypair.from_bytes(base58.b58decode(private_key))
    
    # def record_debt_on_chain(self, debt_details):
    #     try:
    #         metadata = {
    #             **debt_details,
    #             "recorded_at": datetime.utcnow().isoformat(),
    #             "type": "proof_of_debt",
    #             "version": "1.0"
    #         }
            
    #         memo_text = json.dumps(metadata)
            
    #         # Get recent blockhash
    #         latest_blockhash = self.solana_client.get_latest_blockhash().value.blockhash
    #         print(f"Latest blockhash: {latest_blockhash}")
            
    #         # Create instruction
    #         instruction = Instruction(
    #             program_id=self.memo_program_id,
    #             data=memo_text.encode('utf-8'),
    #             accounts=[]
    #         )
            
    #         # Create transaction PROPERLY
    #         transaction = Transaction()
    #         transaction.add(instruction)
    #         transaction.recent_blockhash = latest_blockhash
    #         transaction.fee_payer = self.company_wallet.pubkey()
            
    #         # Sign the transaction
    #         transaction.sign([self.company_wallet])
    #         print(f"Transaction signed by: {self.company_wallet.pubkey()}")
            
    #         # Send transaction
    #         response = self.solana_client.send_transaction(
    #             transaction,
    #             opts=TxOpts(skip_preflight=False, max_retries=3)
    #         )
            
    #         txid = str(response.value)
    #         print(f"Transaction sent! TXID: {txid}")
            
    #         return {
    #             "success": True,
    #             "transaction_id": txid,
    #             "explorer_url": f"https://explorer.solana.com/tx/{txid}?cluster=devnet",
    #             "metadata": metadata
    #         }
            
    #     except Exception as e:
    #         print(f"Blockchain error: {e}")
    #         return {"success": False, "error": str(e)}

    def record_debt_on_chain(self, debt_details):
        try:
            metadata = {
                **debt_details,
                "recorded_at": datetime.utcnow().isoformat(),
                "type": "proof_of_debt",
                "version": "1.0"
            }
            
            memo_text = json.dumps(metadata)
            
            # Get recent blockhash
            latest_blockhash = self.solana_client.get_latest_blockhash().value.blockhash
            print(f"Latest blockhash: {latest_blockhash}")
            
            # Create instruction
            instruction = Instruction(
                program_id=self.memo_program_id,
                data=memo_text.encode('utf-8'),
                accounts=[]
            )
            
            # Create transaction using the NEW method
            from solders.message import Message
            from solders.transaction import VersionedTransaction
            
            # Create message
            message = Message.new_with_blockhash(
                [instruction],
                self.company_wallet.pubkey(),
                latest_blockhash
            )
            
            # Create and sign transaction
            transaction = VersionedTransaction(message, [self.company_wallet])
            print(f"Transaction created and signed by: {self.company_wallet.pubkey()}")
            
            # Send transaction
            response = self.solana_client.send_transaction(
                transaction,
                opts=TxOpts(skip_preflight=False, max_retries=3)
            )
            
            txid = str(response.value)
            print(f"Transaction sent! TXID: {txid}")
            
            return {
                "success": True,
                "transaction_id": txid,
                "explorer_url": f"https://explorer.solana.com/tx/{txid}?cluster=devnet",
                "metadata": metadata
            }
            
        except Exception as e:
            print(f"Blockchain error: {e}")
            return {"success": False, "error": str(e)}
    
    def mint_proof_of_debt_nft(self, debt_metadata, employee_wallet):
        try:
            nft_metadata = {
                "name": f"Proof of Debt - {debt_metadata['employer_name']}",
                "description": f"Verified debt acknowledgment for {debt_metadata['employee_name']}",
                "image": "https://ipfs.io/ipfs/QmX6z6Q7R8RZ5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z",
                "attributes": [
                    {"trait_type": "Debt Amount", "value": debt_metadata['debt_amount']},
                    {"trait_type": "Due Date", "value": debt_metadata['due_date']},
                    {"trait_type": "Employer", "value": debt_metadata['employer_name']},
                    {"trait_type": "Employee", "value": debt_metadata['employee_name']},
                    {"trait_type": "Recorded On", "value": debt_metadata['recorded_at']}
                ]
            }
            
            headers = {
                "X-CLIENT-SECRET": os.getenv('CROSSMINT_API_KEY'),
                "Content-Type": "application/json"
            }
            
            payload = {
                "recipient": f"solana:{employee_wallet}",
                "metadata": nft_metadata,
                "reuploadLinkedFiles": True
            }
            
            collection_id = os.getenv('CROSSMINT_COLLECTION_ID')
            response = requests.post(
                f"https://staging.crossmint.com/api/2022-06-09/collections/{collection_id}/nfts",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                return {
                    "success": True,
                    "nft_id": response.json().get('id'),
                    "nft_metadata": nft_metadata
                }
            else:
                return {"success": False, "error": response.text}
                
        except Exception as e:
            return {"success": False, "error": str(e)}