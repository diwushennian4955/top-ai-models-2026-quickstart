"""
Top Video Generation Models of 2026 — API Demo
Access Kling 3.0, Veo 3, and more via NexaAPI

Get your free API key: https://nexa-api.com
"""
from nexaapi import NexaAPI

client = NexaAPI(api_key='YOUR_API_KEY')  # Get free key at nexa-api.com

# Kling 3.0 — top-ranked video model 2026
print("=== Kling 3.0 — Top-Ranked Video Model 2026 ===")
video = client.video.generate(
    model='kling-v1',
    prompt='Cinematic drone shot over a futuristic city at night, 4K quality',
    duration=5
)
print(f"Video URL: {video.url}")

# Veo 3 — Google's video model
print("\n=== Veo 3 — Google's Video Generation ===")
veo_video = client.video.generate(
    model='veo-3',
    prompt='A timelapse of a flower blooming in a garden, ultra HD',
    duration=5
)
print(f"Veo 3 video URL: {veo_video.url}")

print("\n✅ Top video models accessed via one API!")
print("🔗 nexa-api.com | pip install nexaapi")
