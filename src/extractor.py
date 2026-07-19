import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from src.prompts import prompt
from src.schemas import Resume
print("running app")
load_dotenv()

my_schema = Resume.model_json_schema()

response_format = {"type": "json_object"}

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment is not set")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"


def extract_resume(text: str) -> object:

    print("extracting resume")

    my_prompt = prompt(text, my_schema)

    message = [{"role": "user", "content": my_prompt}]

    response = client.chat.completions.create(
        model=model, messages=message, response_format=response_format
    )

    json_text = response.choices[0].message.content

    resume_json = Resume.model_validate_json(json_text)

    return resume_json
