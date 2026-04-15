import anthropic

client = anthropic.Anthropic()

# Modern approach (recommended for Claude 4.6)
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "adaptive"},  # Let Claude decide
    messages=[{"role": "user", "content": "Your complex question here"}]
)

# Older manual approach (still works, but deprecated)
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[{"role": "user", "content": "Your complex question here"}]
)