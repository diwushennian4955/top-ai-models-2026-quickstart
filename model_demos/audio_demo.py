"""
Top Audio/TTS Models of 2026 — API Demo
Access ElevenLabs-quality voices via NexaAPI

50+ voices, multilingual support
Get your free API key: https://nexa-api.com
"""
from nexaapi import NexaAPI

client = NexaAPI(api_key='YOUR_API_KEY')  # Get free key at nexa-api.com

# ElevenLabs-quality TTS
print("=== Top TTS Model — ElevenLabs Quality ===")
audio = client.audio.tts(
    model='eleven-multilingual-v2',
    text='The future of AI is accessible to every developer. The top models of 2026 are now available via a single API.',
    voice='rachel'
)
print(f"Audio URL: {audio.url}")

# Different voice
print("\n=== Different Voice Style ===")
audio2 = client.audio.tts(
    model='eleven-multilingual-v2',
    text='Welcome to NexaAPI — where all top AI models meet in one place.',
    voice='adam'
)
print(f"Audio URL: {audio2.url}")

print("\n✅ Top TTS models accessed via one API!")
print("🔗 nexa-api.com | pip install nexaapi")
