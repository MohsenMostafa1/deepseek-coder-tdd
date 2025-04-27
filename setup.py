from setuptools import setup, find_packages

setup(
    name="deepseek-coder-tdd",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List your dependencies here from requirements.txt
        "fastapi",
        "uvicorn",
        "transformers",
        "torch",
        "sentence-transformers",
        "hnswlib",
        "sqlalchemy",
        "python-multipart",
        "pyngrok",
        "nest-asyncio",
        "requests",
        "beautifulsoup4"
    ],
    entry_points={
        'console_scripts': [
            'deepseek-coder=app.main:main',
        ],
    },
)
