from dotenv import load_dotenv
import os
from openai import OpenAI
from pathlib import Path



load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env", override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_command(command: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Linux terminal assistant. Explain the following command in plain language for beginners. Keep it short and clear."},
            {"role": "user", "content": command}
        ],
        temperature=0.2,
        max_tokens=50
    )
    return response.choices[0].message.content.strip()





