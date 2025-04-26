# app/utils/helpers.py
import hashlib
import re
import sqlite3
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer

def initialize_database(db_path: str) -> sqlite3.Connection:
    """Initialize SQLite database with schema"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create tables (same as CodeMemory._init_db)
    # ... [table creation queries from original CodeMemory class]
    
    conn.commit()
    return conn

def get_embedding(text: str, model: SentenceTransformer) -> np.ndarray:
    """Generate text embeddings using Sentence Transformer"""
    return model.encode(text)

def validate_code_structure(code: str, language: str) -> bool:
    """Validate code structure using regex patterns"""
    lang_config = Config.SUPPORTED_LANGUAGES.get(language)
    if not lang_config:
        return False
    return any(re.search(pattern, code) for pattern in lang_config["validation_patterns"])

def generate_context_hash(*args) -> str:
    """Generate SHA256 hash for context identification"""
    combined = "".join(str(arg) for arg in args)
    return hashlib.sha256(combined.encode()).hexdigest()

def format_prompt_section(title: str, content: str) -> str:
    """Format a section for the code generation prompt"""
    if not content:
        return f"// {title}: None\n"
    return f"// {title}:\n{content}\n"
