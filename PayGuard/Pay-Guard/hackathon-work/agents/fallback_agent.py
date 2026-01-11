import requests
import os

class FallbackAIAgent:
    def __init__(self):
        self.coral_api_key = os.getenv('CORAL_API_KEY', '')
    
    def generate_fallback_message(self, debt_details):
        """Fallback to Coral V-1 if other AI services fail"""
        try:
            # Simple fallback message generation
            message = f"""
            IMPORTANT: Salary Payment Delay Notification
            
            Dear {debt_details['employer_name']},
            
            This is a formal notification regarding the delayed salary payment for {debt_details['employee_name']}.
            
            Amount: {debt_details['debt_amount']}
            Due Date: {debt_details['due_date']}
            
            This debt has been recorded on the Solana blockchain as immutable proof.
            
            Please arrange for immediate payment to avoid further escalation.
            
            Sincerely,
            PayGuard System
            """
            
            return message.strip()
            
        except Exception as e:
            return f"Error generating fallback message: {str(e)}"