# DeepSeek Code Generation System

An advanced code generation tool with feedback-driven learning and function calling capabilities.

## Features

- AI-powered code generation using DeepSeek 6.7B model
- Feedback-aware code retrieval system
- Code execution sandbox
- Historical context tracking
- Automated code validation and linting
- Function calling integration

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/deepseek-tdd-cicd.git
cd deepseek-tdd-cicd

# Install dependencies
pip install -r requirements.txt

# Initialize database
python -m app.utils.helpers --init-db
