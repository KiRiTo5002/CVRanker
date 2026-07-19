from src.schemas import JobDescription, MatchResult, Resume


SKILL_WEIGHT = 50
EXPERIENCE_WEIGHT = 25
EDUCATION_WEIGHT = 15
CERTIFICATION_WEIGHT = 10



def score_skills(
    resume_skills: list[str],
    required_skills: list[str],
) -> tuple[float, list[str], list[str]]:
    """
    Compare resume skills against required job skills.

    Returns:
        (
            skills_score,
            matched_required_skills,
            missing_required_skills,
        )
    """

    if not required_skills:
        return 100.0, [], []

    resume_set = {
        skill.lower().strip()
        for skill in resume_skills
    }

    required_set = {
        skill.lower().strip()
        for skill in required_skills
    }

    matched = sorted(resume_set & required_set)
    missing = sorted(required_set - resume_set)

    score = (len(matched) / len(required_set)) * 100

    return score, matched, missing


def score_experience(
    resume_years: float,
    minimum_years: float | None,
) -> float:
    """Score the candidate's professional experience."""

    if minimum_years in (None, 0):
        return 100.0

    return min(
        (resume_years / minimum_years) * 100,
        100.0,
    )


def score_education(
    resume_education: list[str],
    required_education: list[str],
) -> float:
    """Score education requirements."""

    if not required_education:
        return 100.0

    resume_text = " ".join(resume_education).lower()

    for requirement in required_education:
        if requirement.lower() in resume_text:
            return 100.0

    return 0.0


def score_certifications(
    resume_certifications: list[str],
    required_certifications: list[str],
) -> float:
    """Score certification requirements."""

    if not required_certifications:
        return 100.0

    resume_set = {
        cert.lower().strip()
        for cert in resume_certifications
    }

    required_set = {
        cert.lower().strip()
        for cert in required_certifications
    }

    matched = resume_set & required_set

    return (len(matched) / len(required_set)) * 100



def score_candidate(
    resume: Resume,
    job_description: JobDescription,
) -> MatchResult:
    """
    Calculate an overall compatibility score between a
    candidate's resume and a job description.
    """

    (
        skills_score,
        matched_required_skills,
        missing_required_skills,
    ) = score_skills(
        resume.skills,
        job_description.required_skills,
    )

    experience_score = score_experience(
        resume.years_of_experience,
        job_description.minimum_years_of_experience,
    )

    education_score = score_education(
        resume.education,
        job_description.required_education,
    )

    certification_score = score_certifications(
        resume.certifications,
        job_description.required_certifications,
    )

    overall_score = (
        skills_score * SKILL_WEIGHT
        + experience_score * EXPERIENCE_WEIGHT
        + education_score * EDUCATION_WEIGHT
        + certification_score * CERTIFICATION_WEIGHT
    ) / 100

    return MatchResult(
        overall_score=round(overall_score, 2),
        skills_score=round(skills_score, 2),
        experience_score=round(experience_score, 2),
        education_score=round(education_score, 2),
        certification_score=round(certification_score, 2),
        matched_required_skills=matched_required_skills,
        missing_required_skills=missing_required_skills,
    )