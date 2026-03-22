"""
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
"""
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# You can set the GEMINI_API_KEY environment variable to your API key before running this code.

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content("Explain AI in simple words")
print(response.text)
