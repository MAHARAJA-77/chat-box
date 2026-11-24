import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a concise travel planner.",
        temperature=0.7,
    ),
    history=[
        types.UserContent(parts=[types.Part(text="I like quiet gardens.")]),
        types.ModelContent(parts=[types.Part(text="Got it—I'll prioritize peaceful spots.")]),
    ],
)

reply = chat.send_message("Give me a morning idea.")
print(reply.text)