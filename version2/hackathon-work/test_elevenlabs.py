# import os
# from elevenlabs import ElevenLabs
# from dotenv import load_dotenv

# # Load your environment variables from .env file
# load_dotenv()

# # Get your API key from environment variables
# api_key = os.getenv('ELEVENLABS_API_KEY')
# print(f"API Key loaded: {api_key[:10]}...")  # Print first 10 chars for safety

# # Initialize the client
# try:
#     client = ElevenLabs(api_key=api_key)
#     print("✅ ElevenLabs client initialized successfully")
# except Exception as e:
#     print(f"❌ Failed to initialize client: {e}")
#     exit()

# # Test getting available voices (this verifies authentication)
# try:
#     voices = client.voices.get_all()
#     print(f"✅ Authentication successful. Found {len(voices.voices)} voices")
#     for voice in voices.voices[:3]:  # Print first 3 voices
#         print(f"  - {voice.name} ({voice.voice_id})")
# except Exception as e:
#     print(f"❌ Authentication failed: {e}")
#     exit()

# # Test text-to-speech generation
# test_text = "Hello, this is a test to see if the Eleven Labs API is working properly."
# try:
#     print(f"🧪 Generating audio for text: '{test_text}'")
    
#     audio = client.text_to_speech(
#         text=test_text,
#         voice="Rachel",  # Use a voice you know exists
#         model="eleven_monolingual_v1"
#     )
    
#     # Save the audio to a file
#     with open("test_output.mp3", "wb") as f:
#         f.write(audio)
    
#     print("✅ Audio generated and saved successfully as 'test_output.mp3'")
#     print("🎧 Play the file to verify the audio quality")

# except Exception as e:
#     print(f"❌ Text-to-speech generation failed: {e}")

import os
from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('ELEVENLABS_API_KEY')

print("🔍 Debugging the ElevenLabs client object...")

# Create the client
client = ElevenLabs(api_key=api_key)

# 1. Print the TYPE of the client
print(f"1. Type of client: {type(client)}")
print(f"   Module: {type(client).__module__}")

# 2. Print all attributes and methods the client has
print(f"\n2. All attributes/methods of client:")
for attr_name in dir(client):
    # Skip private attributes (ones starting with __)
    if not attr_name.startswith('__'):
        attr_value = getattr(client, attr_name)
        print(f"   - {attr_name} (type: {type(attr_value)})")

# 3. Check if text_to_speech exists
print(f"\n3. Has 'text_to_speech'? {hasattr(client, 'text_to_speech')}")
print(f"   Has 'generate'? {hasattr(client, 'generate')}")

# 4. Check if it's callable
print(f"\n4. Is client itself callable? {callable(client)}")