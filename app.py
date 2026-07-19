from pathlib import Path

from src.extractor import extract_jd, extract_resume
from src.parser import extract_text_from_pdf

resume_file = Path("data/resume/dummy_resume_1.pdf")
job_description_file = Path("data/jobs/job_description_1_ai_engineer.pdf")


resume_text = extract_text_from_pdf(resume_file)
resume = extract_resume(resume_text)

job_description_text = extract_text_from_pdf(job_description_file)
job_description = extract_jd(job_description_text)


print(resume)
print(job_description)
