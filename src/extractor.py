import os

from dotenv import load_dotenv
from groq import Groq

from src.prompts import build_resume_prompt, build_jd_prompt
from src.schemas import Resume, JobDescription

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"
RESPONSE_FORMAT = {"type": "json_object"}

resume_schema = Resume.model_json_schema()
jd_schema = JobDescription.model_json_schema()


def extract_resume(text: str) -> Resume:
    """Extract structured information from a resume."""

    prompt = build_resume_prompt(text, resume_schema)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format=RESPONSE_FORMAT,
    )

    json_text = response.choices[0].message.content

    return Resume.model_validate_json(json_text)


def extract_jd(text: str) -> JobDescription:
    """Extract structured information from a job description."""

    prompt = build_jd_prompt(text, jd_schema)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format=RESPONSE_FORMAT,
    )

    json_text = response.choices[0].message.content

    return JobDescription.model_validate_json(json_text)
