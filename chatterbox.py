from google import genai
from google.genai import types
from dotenv import load_dotenv  
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")
client = genai.Client(api_key=API_KEY)  



grounding_tool=types.Tool(
    google_search=types.GoogleSearch()
)


# chat=client.chats.create(model="gemini-2.5-flash")

# userinput=input("\nuser: ")

def generate_response(prompt: str) ->None:
    while(prompt.lower()!="exit"):
        response = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            tools=[grounding_tool],
            system_instruction="Use the provided tools to assist in answering the user's query accurately. also be funny and witty."
        )
    ).send_message(prompt)
    print (response.text)
    prompt = input("\nuser: ")
    




if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    generate_response(user_prompt)