# app/config.py
from enum import Enum

class ToolType(Enum):
    CODE_EXECUTION = "execute_code"
    CODE_LINTING = "lint_code"
    KNOWLEDGE_RETRIEVAL = "get_knowledge"
    CODE_RETRIEVAL = "search_code"
    HISTORY_RETRIEVAL = "get_history"

class Settings:
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    RETRIEVER_MAX_ITEMS = 10000
    RETRIEVER_EF_CONSTRUCTION = 200
    RETRIEVER_M = 16
    MODEL_NAME = "deepseek-ai/deepseek-coder-6.7b-instruct"
    GENERATION_CONFIG = {
        "max_new_tokens": 512,
        "temperature": 0.7,
        "top_p": 0.9,
        "do_sample": True,
        "repetition_penalty": 1.1
    }
    SUPPORTED_LANGUAGES = {
        # ... (same as original Config.SUPPORTED_LANGUAGES)
    }
