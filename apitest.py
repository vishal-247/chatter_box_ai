import os
from google import genai
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise SystemExit(
        "Missing GEMINI_API_KEY. Create a .env file or set the environment variable."
    )

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="hello how are you!"
)
print(response.text)