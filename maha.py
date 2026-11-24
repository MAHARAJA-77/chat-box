import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()


def test_gemini_connection() -> None:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")

    # Initialize the GenAI client with the API key from .env
    client = genai.Client(api_key=api_key)

    prompt = "What can you do? Answer concisely in 4-5 short bullet points."
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    print("Connection successful! Gemini response:\n")
    print(response.text)


if __name__ == "__main__":
    test_gemini_connection()