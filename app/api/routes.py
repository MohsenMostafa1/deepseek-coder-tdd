# app/api/routes.py
from fastapi import APIRouter, HTTPException
from app.services.deepseek_service import DeepSeekService
from app.models import GenerateCodeRequest

router = APIRouter()
service = DeepSeekService()

@router.post("/generate_code")
async def generate_code(request: GenerateCodeRequest):
    try:
        service.initialize_model()
        prompt = construct_prompt(request)
        generated = service.generate_code(prompt)
        return {"code": generated}
    except Exception as e:
        raise HTTPException(500, str(e))

def construct_prompt(request: GenerateCodeRequest):
    # Add prompt construction logic
    return f"Generate {request.language} code for: {request.task_description}"
