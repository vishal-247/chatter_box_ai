from google import genai
from dotenv import load_dotenv
from google.genai import types 
import httpx , pathlib
import os

load_dotenv()
client=genai.Client(api_key=os.getenv("API_KEY"))

# doc_url="https://sample-files.com/downloads/documents/pdf/sample-report.pdf"
# doc_data=httpx.get(doc_url).content

# if you want to use loacl file path then 
file_path=pathlib.Path('./pdf/hgjhh.pdf')
doc_data=file_path.read_bytes()


pdf=types.Part.from_bytes(
    data=doc_data,
    mime_type="application/pdf"
)

prompt:str=input("ask: ")

response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[pdf,prompt],
    config=types.GenerateContentConfig(
        system_instruction="answer within 100 words"
    )
)

print(response.text)