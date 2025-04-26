# tests/test_utils.py
import pytest
from app.utils.helpers import *

def test_validate_code_structure():
    valid_python = "def example():\n    pass"
    assert validate_code_structure(valid_python, "python") is True
    
    invalid_python = "just some text"
    assert validate_code_structure(invalid_python, "python") is False

def test_generate_context_hash():
    hash1 = generate_context_hash("test", "python")
    hash2 = generate_context_hash("test", "python")
    hash3 = generate_context_hash("different", "python")
    
    assert hash1 == hash2
    assert hash1 != hash3

def test_format_prompt_section():
    section = format_prompt_section("Test", "Content")
    assert "// Test:" in section
    assert "Content" in section
