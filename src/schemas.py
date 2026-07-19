from pydantic import BaseModel, Field


class Resume(BaseModel):
    """Structured representation of a candidate's resume."""

    name: str
    email: str | None = None
    linkedin: str | None = None
    phone_number: str | None = None
    overview: str | None = None

    skills: list[str] = Field(default_factory=list)
    work_experience: list[str] = Field(default_factory=list)
    projects: list[str] = Field(default_factory=list)
    education: list[str] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)

    years_of_experience: float


class JobDescription(BaseModel):
    """Structured representation of a job description."""

    required_skills: list[str] = Field(default_factory=list)
    preferred_skills: list[str] = Field(default_factory=list)

    required_education: list[str] = Field(default_factory=list)
    required_certifications: list[str] = Field(default_factory=list)

    minimum_years_of_experience: float | None = None

    job_summary: str | None = None


class MatchResult(BaseModel):
    """Structured representation of how well a candidate matches a job description."""

    overall_score: float

    skills_score: float
    experience_score: float
    education_score: float
    certification_score: float

    matched_required_skills: list[str] = Field(default_factory=list)
    missing_required_skills: list[str] = Field(default_factory=list)