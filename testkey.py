import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

print("Key =", key)

genai.configure(api_key=key)

for model in genai.list_models():
    print(model.name)