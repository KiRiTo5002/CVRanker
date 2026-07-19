import os
import streamlit as st

from dotenv import load_dotenv
from groq import Groq

from src.prompts import (
    build_jd_prompt,
    build_resume_prompt,
)
from src.schemas import (
    JobDescription,
    Resume,
)



load_dotenv()

api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"
RESPONSE_FORMAT = {"type": "json_object"}

RESUME_SCHEMA = Resume.model_json_schema()
JD_SCHEMA = JobDescription.model_json_schema()




def _extract_structured_data(
    prompt: str,
    schema_model,
):
    """
    Send a prompt to the LLM and validate the JSON response
    against the supplied Pydantic model.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        response_format=RESPONSE_FORMAT,
    )

    json_text = response.choices[0].message.content

    return schema_model.model_validate_json(json_text)




def extract_resume(text: str) -> Resume:
    """Extract structured information from a resume."""

    prompt = build_resume_prompt(
        text,
        RESUME_SCHEMA,
    )

    return _extract_structured_data(
        prompt,
        Resume,
    )


def extract_jd(text: str) -> JobDescription:
    """Extract structured information from a job description."""

    prompt = build_jd_prompt(
        text,
        JD_SCHEMA,
    )

    return _extract_structured_data(
        prompt,
        JobDescription,
    )