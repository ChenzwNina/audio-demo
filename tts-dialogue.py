import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = elevenlabs.text_to_dialogue.convert(
    inputs=[
        {
            "text": "Um... I think climate change is, like, becoming harder to ignore these days.",
            "voice_id": "9BWtsMINqrJLrRacOk9x",
        },
        {
            "text": "[Concern] We’re kind of seeing more extreme weather events, you know—",
            "voice_id": "9BWtsMINqrJLrRacOk9x",
        },
        {
            "text": "[interrupting!]—like floods... Sorry go ahead—",
            "voice_id": "1SM7GgM6IMuvQlz2BwM3",
        },
        {
            "text": "—and we should take actions!",
            "voice_id": "9BWtsMINqrJLrRacOk9x",
        },
    ]
)

with open("dialogue.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)

print("Saved to dialogue.mp3")