def build_resume_prompt(text: str, schema: dict) -> str:
    return f"""
You are an expert resume parser working for a recruitment company.

## Task

Extract structured information from the resume and return a valid JSON object that follows the provided schema exactly.

## Rules

- Do not guess or infer information that is not explicitly supported by the resume.
- If a scalar field is missing, return null.
- If a list field is missing, return [].
- Never return null for list fields.
- Return only valid JSON.
- Do not include markdown, explanations, or extra text.
- Follow the provided schema exactly.

## Skills Extraction

Extract ALL professional skills mentioned anywhere in the resume, including:

- Skills section
- Work experience
- Projects
- Certifications
- Professional summary
- Technical tools
- Software
- Programming languages
- Frameworks
- Databases
- Cloud platforms

Return skills as short, normalized skill names.

Examples:

GOOD:
[
    "Python",
    "FastAPI",
    "Docker",
    "SQL",
    "Adobe Premiere Pro",
    "Motion Graphics",
    "Color Grading",
    "Video Editing"
]

BAD:
[
    "Proficient in Adobe Premiere Pro and After Effects",
    "Worked with Docker in previous projects",
    "Knowledge of motion graphics and color grading"
]

Split combined skills.

Example:

"Adobe Premiere Pro and Adobe After Effects"

becomes

[
    "Adobe Premiere Pro",
    "Adobe After Effects"
]

## Experience Calculation

Calculate the candidate's total professional experience in years as a decimal.

Include:

- Full-time positions
- Part-time positions
- Internships
- Apprenticeships
- Freelance work

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

- Do not guess.
- If a scalar field is missing, return null.
- If a list field is missing, return [].
- Never return null for list fields.
- Return only valid JSON.
- Do not include markdown or explanations.
- Follow the schema exactly.

## Skills Extraction

Extract ONLY the individual professional skills required for the role.

Do NOT return complete requirement sentences.

Return concise skill names only.

GOOD:

[
    "Python",
    "FastAPI",
    "Docker",
    "SQL",
    "AWS",
    "Communication",
    "Adobe Premiere Pro",
    "Adobe After Effects",
    "Motion Graphics",
    "Color Grading",
    "Audio Editing"
]

BAD:

[
    "Proficiency in Adobe Premiere Pro and Adobe After Effects",
    "Strong understanding of pacing, storytelling and composition",
    "Experience editing content for YouTube and Instagram"
]

Split compound skills.

Example:

"Adobe Premiere Pro and Adobe After Effects"

becomes

[
    "Adobe Premiere Pro",
    "Adobe After Effects"
]

Example:

"Knowledge of color grading, audio editing, and motion graphics"

becomes

[
    "Color Grading",
    "Audio Editing",
    "Motion Graphics"
]

Extract skills from the entire document, including:

- Required Qualifications
- Preferred Skills
- Responsibilities
- Technical Requirements
- Software Requirements

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