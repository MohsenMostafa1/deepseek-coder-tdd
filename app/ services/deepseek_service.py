import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DeepSeekService:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise ValueError("DeepSeek API key is required")
        
        self.api_url = "https://api.deepseek.com/v1/generate"  # Example URL
    
    def generate_code(self, prompt, language="python", max_tokens=512):
        """Generate code using DeepSeek API based on prompt"""
        if not prompt:
            raise ValueError("Prompt cannot be empty")
        
        response = requests.post(
            self.api_url,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "prompt": prompt,
                "language": language,
                "max_tokens": max_tokens,
                "temperature": 0.7
            }
        )
        
        if response.status_code != 200:
            error_message = f"API Error: {response.status_code}"
            try:
                error_data = response.json()
                error_message = error_data.get("error", error_message)
            except:
                pass
            raise Exception(error_message)
        
        return response.json()
