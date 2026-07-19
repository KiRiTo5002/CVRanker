from pydantic import BaseModel, Field


class Resume(BaseModel):
    """Structured information extracted from a candidate's resume."""

    
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
    """Structured information extracted from a job description."""

    
    required_skills: list[str] = Field(default_factory=list)
    required_education: list[str] = Field(default_factory=list)
    required_certifications: list[str] = Field(default_factory=list)
    minimum_years_of_experience: float | None = None

    
    preferred_skills: list[str] = Field(default_factory=list)

    
    job_summary: str | None = None


class MatchResult(BaseModel):
    """Result of comparing a candidate's resume against a job description."""

    
    overall_score: float = Field(ge=0, le=100)

    
    skills_score: float = Field(ge=0, le=100)
    experience_score: float = Field(ge=0, le=100)
    education_score: float = Field(ge=0, le=100)
    certification_score: float = Field(ge=0, le=100)

    
    matched_required_skills: list[str] = Field(default_factory=list)
    missing_required_skills: list[str] = Field(default_factory=list)