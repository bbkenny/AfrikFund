from flask import Flask, render_template, request, jsonify
from blockchain_agent import PayGuardBlockchainAgent
from ai_agent import PayGuardAIAgent
from fallback_agent import FallbackAIAgent
import threading
import os
from datetime import datetime

app = Flask(__name__)
blockchain_agent = PayGuardBlockchainAgent()
ai_agent = PayGuardAIAgent()
fallback_agent = FallbackAIAgent()

# Create directories if they don't exist
os.makedirs("static/audio", exist_ok=True)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/report-debt', methods=['POST'])
def report_debt():
    try:
        debt_data = request.json
        print(f"Received debt report: {debt_data}")
        
        # Validate required fields
        required_fields = ['employer_name', 'employee_name', 'employee_wallet', 'debt_amount', 'due_date']
        for field in required_fields:
            if field not in debt_data:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        # 1. Record on blockchain
        blockchain_result = blockchain_agent.record_debt_on_chain(debt_data)
        
        if not blockchain_result['success']:
            return jsonify({"error": f"Blockchain error: {blockchain_result['error']}"}), 500
        
        # 2. Mint NFT
        nft_result = blockchain_agent.mint_proof_of_debt_nft(
            blockchain_result['metadata'],
            debt_data['employee_wallet']
        )
        
        # 3. Generate follow-up (async)
        threading.Thread(target=process_ai_followup, args=(debt_data,)).start()
        
        response_data = {
            "success": True,
            "blockchain": {
                "transaction_id": blockchain_result['transaction_id'],
                "explorer_url": blockchain_result['explorer_url']
            },
            "nft": {
                "minted": nft_result['success'],
                "nft_id": nft_result.get('nft_id'),
                "error": nft_result.get('error')
            }
        }
        
        return jsonify(response_data)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def process_ai_followup(debt_data):
    """Process AI follow-up asynchronously"""
    try:
        # Try Mistral AI first
        message = ai_agent.generate_follow_up_message(debt_data)
    except:
        # Fallback to simple message generation
        message = fallback_agent.generate_fallback_message(debt_data)
    
    try:
        # Try to generate audio
        audio_file = ai_agent.generate_audio_update(message)
    except:
        audio_file = None
    
    print(f"\n📧 Generated Message:\n{message}")
    if audio_file:
        print(f"🎵 Audio file generated: {audio_file}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)