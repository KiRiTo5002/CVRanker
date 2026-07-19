COMMON_RULES = """
## Rules
- Do not guess or infer information that is not explicitly present.
- If a field is missing, return null for single-value fields or an empty list for list fields.
- Do not include fields that are not defined in the provided schema.
- Return only valid JSON.
- Do not include explanations, markdown, or additional text.
- Follow the provided schema exactly.
"""


EXPERIENCE_EXAMPLES = """
Examples:
- 6 months → 0.5
- 1 year 3 months → 1.25
- 2 years 6 months → 2.5
"""


def build_resume_prompt(text: str, schema: dict) -> str:
    """Build the prompt used to extract structured information from a resume."""

    return f"""
You are an expert resume parser working for a recruitment company.

## Task
Extract structured information from the candidate's resume.

{COMMON_RULES}

## Experience Calculation
Calculate the candidate's total professional experience as a decimal number of years.

Include:
- Full-time employment
- Part-time professional employment
- Internships
- Apprenticeships

{EXPERIENCE_EXAMPLES}

## Resume
{text}

## JSON Schema
{schema}
"""


def build_jd_prompt(text: str, schema: dict) -> str:
    """Build the prompt used to extract structured information from a job description."""

    return f"""
You are an expert job description parser working for a recruitment company.

## Task
Extract structured information from the job description.

{COMMON_RULES}

## Experience Extraction
Extract the minimum required professional experience as a decimal number of years.

{EXPERIENCE_EXAMPLES}

## Job Description
{text}

## JSON Schema
{schema}
"""