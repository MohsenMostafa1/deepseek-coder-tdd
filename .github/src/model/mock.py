from unittest.mock import MagicMock

class MockDeepSeekCoder:
    def __init__(self):
        self.device = "cuda"
        self.generate = MagicMock(return_value="def mock_function(): return 'mock_output'")
