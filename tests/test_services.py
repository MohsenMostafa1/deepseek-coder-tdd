# tests/test_services.py
import pytest
from unittest.mock import MagicMock
from app.services.deepseek_service import FeedbackAwareRetriever, CodeMemory, CodeExecutor

@pytest.fixture
def mock_db():
    import sqlite3
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

def test_feedback_retriever():
    retriever = FeedbackAwareRetriever()
    test_code = "def test():\n    pass"
    retriever.add_code(test_code, language="python")
    
    results = retriever.search_code("test function", language_filter="python")
    assert len(results) > 0
    assert "test()" in results[0]['code']

def test_code_memory(mock_db):
    memory = CodeMemory()
    memory.conn = mock_db
    
    history_id = memory.add_history(
        "test query", 
        "print('hello')", 
        "python"
    )
    assert isinstance(history_id, int)
    
    history = memory.get_recent_history(limit=1)
    assert len(history) == 1

def test_code_executor():
    executor = CodeExecutor()
    result = executor.lint_code("print('hello')", "python")
    assert "success" in result
