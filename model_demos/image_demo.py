"""
Top Image Generation Models of 2026 — API Demo
Access FLUX Pro, Stable Diffusion 3.5, and more via NexaAPI

Pricing: $0.003/image (85% cheaper than OpenAI)
Get your free API key: https://nexa-api.com
"""
from nexaapi import NexaAPI

client = NexaAPI(api_key='YOUR_API_KEY')  # Get free key at nexa-api.com

# FLUX Pro — top-ranked image model 2026
print("=== FLUX Pro — Top-Ranked Image Model 2026 ===")
image = client.image.generate(
    model='flux-pro',
    prompt='A breathtaking mountain landscape at golden hour, photorealistic, award-winning photography',
    width=1024,
    height=1024
)
print(f"Image URL: {image.url}")

# FLUX Schnell — fast generation
print("\n=== FLUX Schnell — Ultra-Fast Generation ===")
fast_image = client.image.generate(
    model='flux-schnell',
    prompt='A futuristic city skyline at night, neon lights, cyberpunk aesthetic',
    width=1024,
    height=1024
)
print(f"Fast image URL: {fast_image.url}")

# Stable Diffusion 3.5 — high quality
print("\n=== Stable Diffusion 3.5 — High Quality ===")
sd_image = client.image.generate(
    model='stable-diffusion-3-5-large',
    prompt='A serene Japanese garden with cherry blossoms, traditional architecture',
    width=1024,
    height=1024
)
print(f"SD3.5 image URL: {sd_image.url}")

print("\n✅ Top image models accessed at $0.003/image!")
print("🔗 nexa-api.com | pip install nexaapi")
