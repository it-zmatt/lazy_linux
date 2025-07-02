from dotenv import load_dotenv
import os
from openai import OpenAI
from pathlib import Path



load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env", override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_shell_command(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Linux shell command generator. Always respond with just the command."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=50
    )
    return response.choices[0].message.content.strip()



