from google import genai
from  google.genai import types
import os

from dotenv import load_dotenv

load_dotenv()

# userinput=input("\nuser: ")

# ------------------------------------simple bot with no chat history----------------------------------------
# while(userinput.lower()!="exit"):
#     genai_response=client.models.generate_content(
#         model="gemini-2.5-flash", contents=userinput,
#         config=types.GenerateContentConfig(
#             temperature=0.2,
#             system_instruction="answer in 1 line and within 50 words" )
#         )
#     print("bot: ", genai_response.text)
#     userinput=input("\nuser: ")

client=genai.Client(api_key=
                    os.getenv("API_KEY")
)
chat=client.chats.create(model="gemini-2.5-flash")

userinput=input("\nuser: ")
while(userinput.lower()!="exit"):
    response=chat.send_message(userinput)
    print("bot: ", response.text)
    userinput=input("\nuser: ")

# for message in chat.get_history():
#     print(f"{message.role}: {message.parts[0].text}\n")


