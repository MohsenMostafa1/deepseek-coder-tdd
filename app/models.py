# app/models.py
from pydantic import BaseModel
from typing import Optional

class KnowledgeItem(BaseModel):
    content: str
    language: str
    source: Optional[str] = None
    category: Optional[str] = None

class FeedbackRequest(BaseModel):
    history_id: int
    score: float
    notes: Optional[str] = None

class GenerateCodeRequest(BaseModel):
    task_description: str
    language: str = "python"
    context: Optional[str] = None
    project_hash: Optional[str] = None
    category: Optional[str] = None

# Add other request/response models...
