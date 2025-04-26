# app/services/deepseek_service.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer
from .config import Settings

settings = Settings()

class DeepSeekService:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.embedding_model = None
        
    def initialize_model(self):
        try:
            self.embedding_model = SentenceTransformer(
                settings.EMBEDDING_MODEL,
                device="cuda" if torch.cuda.is_available() else "cpu"
            )
            
            self.model = AutoModelForCausalLM.from_pretrained(
                settings.MODEL_NAME,
                torch_dtype=torch.float16,
                device_map="auto",
                low_cpu_mem_usage=True
            )
            self.tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_NAME)
            
        except Exception as e:
            raise RuntimeError(f"Model initialization failed: {str(e)}")

    def generate_code(self, prompt: str):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        return self.model.generate(
            **inputs,
            **settings.GENERATION_CONFIG,
            pad_token_id=self.tokenizer.eos_token_id
        )

# Add other service classes (Retriever, Memory, Executor)...
