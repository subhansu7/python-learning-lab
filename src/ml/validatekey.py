import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Say hello in one word."
    )
    print("API key is valid")
    print(response.output_text)
except Exception as e:
    print("API key is invalid or there is another issue:")
    print(e)