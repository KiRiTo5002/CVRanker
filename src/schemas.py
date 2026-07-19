from pydantic import BaseModel

class Resume(BaseModel): 
    name : str
    email: str |None = None
    linkedin: str |None = None
    phone_number: str |None = None
    skills: list[str]
    work_experience: list[str]
    overview: str |None = None
    projects: list[str]
    education: list[str]
    certifications: list[str]
    years_of_experience: float