# # import requests
# # import os
# # from datetime import datetime
# # from elevenlabs import generate, set_api_key

# # class PayGuardAIAgent:
# #     def __init__(self):
# #         self.mistral_api_key = os.getenv('MISTRAL_API_KEY')
# #         self.elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')
# #         set_api_key(self.elevenlabs_api_key)
    
# #     def generate_follow_up_message(self, debt_details):
# #         prompt = f"""
# #         Create a professional but firm follow-up message regarding delayed salary payment.
        
# #         Employer: {debt_details['employer_name']}
# #         Employee: {debt_details['employee_name']}
# #         Amount: {debt_details['debt_amount']}
# #         Due Date: {debt_details['due_date']}
        
# #         The message should:
# #         - Be professional but assertive
# #         - Mention the proof has been recorded on blockchain
# #         - Request immediate payment
# #         - Mention potential next steps if not resolved
# #         - Be concise (under 200 words)
# #         """
        
# #         response = requests.post(
# #             "https://api.mistral.ai/v1/chat/completions",
# #             headers={"Authorization": f"Bearer {self.mistral_api_key}"},
# #             json={
# #                 "model": "mistral-medium",
# #                 "messages": [{"role": "user", "content": prompt}],
# #                 "max_tokens": 300
# #             }
# #         )
        
# #         return response.json()['choices'][0]['message']['content']
    
# #     def generate_audio_update(self, text_message):
# #         try:
# #             audio = generate(
# #                 text=text_message,
# #                 voice="Bella",
# #                 model="eleven_monolingual_v1"
# #             )
            
# #             filename = f"audio_update_{datetime.now().timestamp()}.mp3"
# #             with open(f"static/audio/{filename}", "wb") as f:
# #                 f.write(audio)
            
# #             return filename
# #         except:
# #             return None

# import requests
# import os
# from datetime import datetime

# # Try to import ElevenLabs with new API, fallback if not available
# try:
#     from elevenlabs.client import ElevenLabs
#     ELEVENLABS_AVAILABLE = True
# except ImportError:
#     ELEVENLABS_AVAILABLE = False
#     print("⚠️  ElevenLabs not available - audio features disabled")

# class PayGuardAIAgent:
#     def __init__(self):
#         self.mistral_api_key = os.getenv('MISTRAL_API_KEY')
#         self.elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')
        
#         # Initialize ElevenLabs client if available
#         if ELEVENLABS_AVAILABLE and self.elevenlabs_api_key:
#             self.elevenlabs_client = ElevenLabs(api_key=self.elevenlabs_api_key)
#         else:
#             self.elevenlabs_client = None
#             print("🔇 ElevenLabs audio disabled - no API key or package not available")
    
#     def generate_follow_up_message(self, debt_details):
#         """
#         Generate professional follow-up message using Mistral AI
#         This creates a formal message to send to employers about delayed payments
#         """
#         prompt = f"""
#         Create a professional but firm follow-up message regarding delayed salary payment.
        
#         Employer: {debt_details['employer_name']}
#         Employee: {debt_details['employee_name']}
#         Amount: {debt_details['debt_amount']}
#         Due Date: {debt_details['due_date']}
        
#         The message should:
#         - Be professional but assertive
#         - Mention the proof has been recorded on blockchain
#         - Request immediate payment
#         - Mention potential next steps if not resolved
#         - Be concise (under 200 words)
#         Include a note that this debt has been immutably recorded on the Solana blockchain.
#         """
        
#         try:
#             response = requests.post(
#                 "https://api.mistral.ai/v1/chat/completions",
#                 headers={"Authorization": f"Bearer {self.mistral_api_key}"},
#                 json={
#                     "model": "mistral-medium",
#                     "messages": [{"role": "user", "content": prompt}],
#                     "max_tokens": 300,
#                     "temperature": 0.7
#                 }
#             )
            
#             if response.status_code == 200:
#                 return response.json()['choices'][0]['message']['content']
#             else:
#                 return f"Error: Mistral API returned status {response.status_code}. Please check your API key."
                
#         except Exception as e:
#             return f"Error generating message: {str(e)}"
    
#     def generate_audio_update(self, text_message):
#         """
#         Generate audio version of the message using ElevenLabs
#         Returns the filename of the generated audio file, or None if failed
#         """
#         if not self.elevenlabs_client:
#             print("⚠️  ElevenLabs not configured - skipping audio generation")
#             return None
            
#         try:
#             # Generate audio using the new ElevenLabs API
#             audio_response = self.elevenlabs_client.generate(
#                 text=text_message,
#                 voice="Bella",  # Professional female voice
#                 model="eleven_monolingual_v1"
#             )
            
#             # Create filename with timestamp
#             filename = f"audio_update_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
            
#             # Save audio to file
#             with open(f"static/audio/{filename}", "wb") as f:
#                 for chunk in audio_response:
#                     if chunk:
#                         f.write(chunk)
            
#             print(f"✅ Audio generated: {filename}")
#             return filename
            
#         except Exception as e:
#             print(f"❌ Audio generation failed: {e}")
#             return None
    
#     def generate_complete_followup(self, debt_details):
#         """
#         Complete workflow: Generate text message + audio version
#         Returns both the text message and audio filename
#         """
#         text_message = self.generate_follow_up_message(debt_details)
#         audio_filename = self.generate_audio_update(text_message)
        
#         return {
#             "text_message": text_message,
#             "audio_filename": audio_filename,
#             "timestamp": datetime.now().isoformat()
#         }

import requests
import os
import time
from datetime import datetime

# Try to import ElevenLabs with new API, fallback if not available
try:
    from elevenlabs.client import ElevenLabs
    ELEVENLABS_AVAILABLE = True
except ImportError:
    ELEVENLABS_AVAILABLE = False
    print("⚠️  ElevenLabs not available - audio features disabled")

class PayGuardAIAgent:
    def __init__(self):
        self.mistral_api_key = os.getenv('MISTRAL_API_KEY')
        self.elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')
        
        # Initialize ElevenLabs client if available
        if ELEVENLABS_AVAILABLE and self.elevenlabs_api_key:
            self.elevenlabs_client = ElevenLabs(api_key=self.elevenlabs_api_key)
        else:
            self.elevenlabs_client = None
            print("🔇 ElevenLabs audio disabled - no API key or package not available")
    
    def generate_follow_up_message(self, debt_details):
        """
        Generate professional follow-up message using Mistral AI
        with smart retry logic for rate limits
        """
        prompt = f"""
        Create a professional but firm follow-up message regarding delayed salary payment.
        
        Employer: {debt_details['employer_name']}
        Employee: {debt_details['employee_name']}
        Amount: {debt_details['debt_amount']}
        Due Date: {debt_details['due_date']}
        
        The message should:
        - Be professional but assertive
        - Mention the proof has been recorded on Solana blockchain
        - Request immediate payment
        - Mention potential legal consequences if not resolved
        - Be concise (under 200 words)
        - Include that this is an automated message from PayGuard system
        """
        
        max_retries = 3
        retry_delay = 2  # seconds
        
        for attempt in range(max_retries):
            try:
                print(f"🤖 Generating AI message (Attempt {attempt + 1}/{max_retries})...")
                
                response = requests.post(
                    "https://api.mistral.ai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.mistral_api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "mistral-medium",  # Using the reliable model
                        "messages": [{
                            "role": "user", 
                            "content": prompt
                        }],
                        "max_tokens": 350,
                        "temperature": 0.7,
                        "top_p": 0.9
                    },
                    timeout=15
                )
                
                if response.status_code == 200:
                    message = response.json()['choices'][0]['message']['content']
                    print("✅ AI message generated successfully!")
                    return message
                    
                elif response.status_code == 429:  # Rate limit
                    wait_time = retry_delay * (attempt + 1)
                    print(f"⏳ Rate limited. Waiting {wait_time}s before retry...")
                    time.sleep(wait_time)
                    continue
                    
                else:
                    error_msg = f"API Error {response.status_code}: {response.text[:100]}..."
                    print(f"❌ {error_msg}")
                    return self._generate_fallback_message(debt_details)
                    
            except requests.exceptions.Timeout:
                print(f"⏰ Request timeout. Retrying in {retry_delay}s...")
                time.sleep(retry_delay)
                continue
                
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                return self._generate_fallback_message(debt_details)
        
        print("⚠️  All retries failed. Using fallback message.")
        return self._generate_fallback_message(debt_details)
    
    def _generate_fallback_message(self, debt_details):
        """Generate a professional fallback message locally"""
        return f"""
Subject: Formal Notice Regarding Delayed Salary Payment - {debt_details['employee_name']}

Dear {debt_details['employer_name']},

I am writing to formally address the outstanding salary payment for {debt_details['employee_name']}. 

The amount of {debt_details['debt_amount']} was due on {debt_details['due_date']} and remains unpaid.

Please be advised that this debt obligation has been immutably recorded on the Solana blockchain as verifiable proof through our PayGuard system.

We require immediate payment to resolve this matter. Failure to remit payment may result in further action as permitted by law.

This is an automated message from the PayGuard debt verification system.

Sincerely,
PayGuard Automated System
"""
    
    def generate_audio_update(self, text_message):
        """
        Generate audio version of the message using ElevenLabs
        """
        if not self.elevenlabs_client:
            print("🔇 ElevenLabs not configured - skipping audio generation")
            return None
            
        try:
            print("🎵 Generating audio version...")
            
            audio_response = self.elevenlabs_client.generate(
                text=text_message,
                voice="Bella",
                model="eleven_monolingual_v1"
            )
            
            filename = f"audio_update_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
            
            with open(f"static/audio/{filename}", "wb") as f:
                for chunk in audio_response:
                    if chunk:
                        f.write(chunk)
            
            print(f"✅ Audio generated: {filename}")
            return filename
            
        except Exception as e:
            print(f"❌ Audio generation failed: {e}")
            return None
    
    def generate_complete_followup(self, debt_details):
        """
        Complete workflow: Generate text message + audio version
        """
        print("🚀 Starting complete follow-up generation...")
        text_message = self.generate_follow_up_message(debt_details)
        audio_filename = self.generate_audio_update(text_message)
        
        return {
            "text_message": text_message,
            "audio_filename": audio_filename,
            "timestamp": datetime.now().isoformat(),
            "success": True if text_message else False
        }