import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
if not API_KEY:
    print("Error: ELEVENLABS_API_KEY not set in .env")
    exit(1)

# ---- Edit your content here ----
text = """
[Surprise] I did not know that. That’s new to me.
"""
# ---- End of content ----

output_file = f"audio/tts-surprise.mp3"
voice_id = "XA2bIQ92TabjGbpO2xRr"  

response = requests.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
    headers={
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
    },
    json={
        "text": text.strip(),
        "model_id": "eleven_v3",
    },
)

if not response.ok:
    print(f"ElevenLabs API error ({response.status_code}): {response.text}")
    exit(1)

with open(output_file, "wb") as f:
    f.write(response.content)

print(f"Audio saved to: {output_file} ({len(response.content)} bytes)")
