from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.services.deepseek_service import DeepSeekService

router = APIRouter()

class GenerateRequest(BaseModel):
    prompt: str
    language: str = "python"
    max_tokens: int = 512

@router.post("/generate")
async def generate_code(request: GenerateRequest, 
                        service: DeepSeekService = Depends()):
    try:
        result = service.generate_code(
            prompt=request.prompt,
            language=request.language,
            max_tokens=request.max_tokens
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
