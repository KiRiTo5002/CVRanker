from pathlib import Path
from src.parser import extract_text_from_pdf
from src.extractor import extract_resume

file = Path("data/resume/dummy_resume_1.pdf")

resume_text = extract_text_from_pdf(file)
resume_json = extract_resume(resume_text)

print(resume_json)