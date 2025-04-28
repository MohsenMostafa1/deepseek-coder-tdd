from setuptools import setup, find_packages

setup(
    name="deepseek-coder-tdd",
    version="0.1",
    packages=find_packages(where="src/app"),  # Explicit path to your app package
    package_dir={
        "app": "src/app",                    # Maps app package to src/app
        "app.services": "src/app/services",  # Explicit subpackage mapping
        "app.utils": "src/app/utils"
    },
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
    include_package_data=True,
    package_data={
        "app": ["*.ini", "*.txt"],  # Include any non-code files
    },
)
