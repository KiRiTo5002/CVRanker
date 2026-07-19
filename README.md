# CVRanker

CVRanker is an AI-powered resume screening application that automatically extracts structured information from resumes and job descriptions using Large Language Models (LLMs), then ranks candidates based on how well they match a job description.

## Current Features

- Extract text from PDF resumes
- Extract text from PDF job descriptions
- Convert unstructured text into structured data using LLMs
- Validate extracted data using Pydantic

## Tech Stack

- Python
- Groq API
- Llama 3.3 70B
- PyMuPDF
- Pydantic
- python-dotenv

## Project Structure

```
CVRanker/
├── app.py
├── data/
├── src/
│   ├── parser.py
│   ├── extractor.py
│   ├── prompts.py
│   └── schemas.py
└── README.md
```

## Roadmap

- [x] PDF Text Extraction
- [x] Resume Information Extraction
- [x] Job Description Information Extraction
- [ ] Candidate Scoring
- [ ] Candidate Ranking
- [ ] Streamlit Interface
- [ ] Deployment
