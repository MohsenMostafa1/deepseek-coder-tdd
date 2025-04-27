from fastapi import FastAPI
from app.api.routes import router as api_router
from app.services.deepseek_service import DeepSeekService
from app.utils.helpers import some_helper_function


app = FastAPI(title="DeepSeek Code Generator")
app.include_router(api_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "healthy"}
