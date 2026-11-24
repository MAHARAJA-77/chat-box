import sys
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Ensures Unicode characters print cleanly in Windows PowerShell
sys.stdout.reconfigure(encoding="utf-8")

# Loads GEMINI_API_KEY from your .env file
load_dotenv()

client = genai.Client()

prompt = "Explain how streaming responses work in APIs in 4 short bullet points."

# Start timer right before sending the request
start_time = time.perf_counter()
first_token_time = None

response_stream = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=400,
    ),
)

last_chunk = None
for chunk in response_stream:
    last_chunk = chunk
    if chunk.text:
        if first_token_time is None:
            first_token_time = time.perf_counter()  # Record when first text arrives
        print(chunk.text, end="", flush=True)

end_time = time.perf_counter()

# Calculate timings
total_time = end_time - start_time
ttft = (first_token_time - start_time) if first_token_time else total_time

print("\n\n--- Timing & Metadata ---")
print(f"First Token Time: {ttft:.2f} sec")
print(f"Total Time:       {total_time:.2f} sec")

if last_chunk:
    if last_chunk.candidates:
        print(f"Finish Reason:    {last_chunk.candidates[0].finish_reason}")

    usage = last_chunk.usage_metadata
    if usage:
        print(f"Prompt Tokens:    {usage.prompt_token_count}")
        print(f"Output Tokens:    {usage.candidates_token_count}")
        print(f"Thinking Tokens:  {usage.thoughts_token_count}")
        print(f"Total Tokens:     {usage.total_token_count}")