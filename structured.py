from google import genai
from dotenv import load_dotenv
import os
from pydantic import BaseModel


class Recipe(BaseModel):
    recipe_name: str 
    ingredients: list[str]





load_dotenv()

client=genai.Client(api_key=os.getenv("API_KEY"))

 
prompt="tell me a joke in one line"
response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config={
         "response_mime_type":"application/json",
         "response_schema": list[Recipe]
    }
)

print(response.text)
