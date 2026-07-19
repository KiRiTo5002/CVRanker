from pathlib import Path

from src.parser import extract_text_from_pdf
from src.extractor import extract_resume, extract_jd
from src.scorer import score_candidate
from src.ranker import rank_candidates


resume_folder = Path("data/resume")
job_description_file = Path("data/jobs/job_description_1_ai_engineer.pdf")


# Extract the job description once
job_description_text = extract_text_from_pdf(job_description_file)
job_description = extract_jd(job_description_text)


# Store (Resume, MatchResult) pairs
candidates = []


# Process every resume
for resume_file in resume_folder.glob("*.pdf"):

    resume_text = extract_text_from_pdf(resume_file)
    resume = extract_resume(resume_text)

    match_result = score_candidate(
        resume,
        job_description,
    )

    candidates.append((resume, match_result))


# Rank candidates
ranked_candidates = rank_candidates(candidates)


# Display results
print("\n===== Ranked Candidates =====\n")

for rank, (resume, match) in enumerate(ranked_candidates, start=1):

    print(f"{rank}. {resume.name}")
    print(f"Overall Score: {match.overall_score}%")
    print(f"Matched Skills: {match.matched_required_skills}")
    print(f"Missing Skills: {match.missing_required_skills}")
    print("-" * 50)