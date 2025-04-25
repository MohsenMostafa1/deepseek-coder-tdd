from fastapi import FastAPI, Depends
from app.api.routes import router
from app.services.deepseek_service import DeepSeekService

app = FastAPI(title="DeepSeek Code Generator API")

def get_service():
    """Dependency to provide DeepSeekService instance"""
    return DeepSeekService()

# Include API routes
app.include_router(router, prefix="/api", dependencies=[Depends(get_service)])

@app.get("/")
async def root():
    return {"status": "ok", "message": "DeepSeek Code Generator API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
