import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

client = genai.GenerativeModel(model_name='gemini-2.0-flash-001')

response = client.generate_content('Why is the 5 + 4')
print(response.text)