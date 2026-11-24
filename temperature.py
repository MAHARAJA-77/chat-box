import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Ensures Unicode characters print cleanly in Windows PowerShell
sys.stdout.reconfigure(encoding="utf-8")

# Loads GEMINI_API_KEY from your .env file
load_dotenv()

client = genai.Client()

prompt = "Explain how streaming responses work in APIs in 4 short bullet points."

response_stream = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=400,
    ),
)

for chunk in response_stream:
    if chunk.text:
        print(chunk.text, end="", flush=True)

print()