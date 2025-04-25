from pydantic import BaseSettings

class Settings(BaseSettings):
    # DeepSeek API Configuration
    deepseek_api_key: str
    deepseek_api_url: str = "https://api.deepseek.com/v1/generate"
    
    # Model Configuration
    model_name: str = "deepseek-ai/deepseek-coder-6.7b-instruct"
    max_tokens: int = 512
    temperature: float = 0.7
    top_p: float = 0.9
    
    # Application Settings
    debug: bool = False
    environment: str = "development"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
