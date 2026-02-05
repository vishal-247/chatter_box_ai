from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
load_dotenv()
client=genai.Client(api_key=os.getenv("API_KEY"))

grounding_tool=types.Tool(
    google_search=types.GoogleSearch()
)


response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents="who won the world cup in 2024?"
    ,config=types.GenerateContentConfig(
        tools=[grounding_tool],
        
        )
    )


print(response)