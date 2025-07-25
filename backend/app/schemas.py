#app/schemas.py
# This module defines the data schemas used in the application.
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# --- User ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# --- CV Sub-sections ---
class CVExperience(BaseModel):
    role: str
    company: str
    client: str
    contract: str
    level: str
    ral: str
    start_date: str  # formato: "YYYY-MM"
    end_date: Optional[str] = None
    description: Optional[str] = None
    current: Optional[bool] = False  # 👈 aggiunto per evitare errori
    tools: Optional[str] = None  # 👈 aggiunto

class CVEducation(BaseModel):
    degree: str
    institution: str
    year: str  # può rimanere anche come stringa tipo "2019" o "2021-2023"
    ongoing: Optional[bool] = False  # 👈 nuovo campo per "in corso"

class CVSkill(BaseModel):
    name: str
    level: Optional[str] = None  # es: Beginner, Intermediate, Expert

class CVProject(BaseModel):
    title: str
    description: Optional[str] = None
    link: Optional[str] = None

class CVCertification(BaseModel):
    name: str
    issuer: Optional[str] = None
    year: Optional[str] = None

class CVSocialProfile(BaseModel):
    platform: str  # es. LinkedIn, GitHub
    url: str       # e
    
class CVLanguage(BaseModel):
    name: str
    level: Optional[str] = None  # es: Base, Intermedio, Fluente, etc.

class CVPersonalInfo(BaseModel):
    full_name: str
    phone: str
    email: str
    birth_date: Optional[str] = None
    address: Optional[str] = None
    website: Optional[str] = None
    nationality: Optional[str] = None  # 👈 aggiunto
    gender: Optional[str] = None       # 👈 aggiunto
    social_profiles: Optional[List[CVSocialProfile]] = []

class CVData(BaseModel):
    personal_info: CVPersonalInfo  # 👈 aggiunto
    profile: Optional[str] = None
    summary: Optional[str] = None
    objectives: Optional[str] = None
    experiences: List[CVExperience] = []
    education: List[CVEducation] = []
    skills: List[CVSkill] = []
    soft_skills: Optional[List[str]] = []
    languages: Optional[List[CVLanguage]] = []
    projects: Optional[List[CVProject]] = []
    certifications: Optional[List[CVCertification]] = []


# --- CV Main Models ---
class CVBase(BaseModel):
    title: str
    category: Optional[str] = None  # ← aggiunto qui
    data: CVData

class CVCreate(CVBase):
    pass

class CVUpdate(CVBase):
    pass

class CVOut(CVBase):
    id: str
    user_email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # compatibile con Pydantic v2
