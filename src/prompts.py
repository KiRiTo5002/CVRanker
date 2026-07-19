def build_resume_prompt(text: str, schema: dict) -> str:
    return f"""
You are an expert resume parser working for a recruitment company.

## Task
Extract structured information from the resume and return a valid JSON object that follows the provided schema exactly.

## Rules
- Do not guess or infer information that is not explicitly present in the resume.
- If a field is missing, return null for single-value fields or an empty list for list fields.
- Do not include fields that are not defined in the provided schema.
- Return only valid JSON. Do not include explanations, markdown, or additional text.
- Follow the schema exactly.

## Experience Calculation
Calculate the candidate's total professional experience as a decimal number of years.
Include internships, apprenticeships, and full-time professional roles.

Examples:
- 6 months → 0.5
- 1 year 3 months → 1.25
- 2 years 6 months → 2.5

## Resume
{text}

## JSON Schema
{schema}
"""


def build_jd_prompt(text: str, schema: dict) -> str:
    return f"""
You are an expert job description parser working for a recruitment company.

## Task
Extract structured information from the job description and return a valid JSON object that follows the provided schema exactly.

## Rules
- Do not guess or infer information that is not explicitly present in the job description.
- If a field is missing, return null for single-value fields or an empty list for list fields.
- Do not include fields that are not defined in the provided schema.
- Return only valid JSON. Do not include explanations, markdown, or additional text.
- Follow the schema exactly.

## Experience Extraction
Extract the minimum required professional experience as a decimal number of years.

Examples:
- 6 months → 0.5
- 1 year 3 months → 1.25
- 2 years 6 months → 2.5

## Job Description
{text}

## JSON Schema
{schema}
"""