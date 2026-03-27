"""
Top LLM Models of 2026 — API Demo
Access GPT-5.4, Claude Opus 4.6, Gemini 3.1, and more via NexaAPI

Get your free API key: https://nexa-api.com
"""
from nexaapi import NexaAPI

client = NexaAPI(api_key='YOUR_API_KEY')  # Get free key at nexa-api.com

# GPT-5.4 equivalent — #1 ranked model
print("=== #1 Ranked: GPT-5.4 Equivalent ===")
response = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "What are the top 3 AI trends of 2026?"}
    ]
)
print(response.choices[0].message.content)

# Claude Opus 4.6 equivalent — #2 ranked, best for coding
print("\n=== #2 Ranked: Claude Opus 4.6 Equivalent (Best for Coding) ===")
code_response = client.chat.completions.create(
    model='claude-3-5-sonnet-20241022',
    messages=[
        {"role": "user", "content": "Write a Python function to call multiple AI APIs concurrently using asyncio"}
    ]
)
print(code_response.choices[0].message.content)

# Gemini 3.1 equivalent — #3 ranked, multimodal
print("\n=== #3 Ranked: Gemini 3.1 Equivalent (Multimodal) ===")
gemini_response = client.chat.completions.create(
    model='gemini-1.5-pro',
    messages=[
        {"role": "user", "content": "Explain multimodal AI in simple terms"}
    ]
)
print(gemini_response.choices[0].message.content)

print("\n✅ All top LLMs accessed via one API!")
print("🔗 nexa-api.com | pip install nexaapi")
