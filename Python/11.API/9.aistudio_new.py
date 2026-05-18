# pip install google-genai
# pip uninstall google-generativeai
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="오늘 저녁에 등 운동 뭐하면 좋을지 정해줘"
)

print(response.text)