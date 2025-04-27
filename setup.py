from setuptools import setup, find_packages

setup(
    name="deepseek_coder",
    version="1.0.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "torch>=1.9.0",
        "transformers>=4.12.0",
        "sentence-transformers>=2.2.0",
        "hnswlib>=0.6.2",
        "python-dotenv>=0.19.0",
        "sqlalchemy>=1.4.0",
        "pytest>=6.2.4"
    ],
    extras_require={
        'dev': [
            'pytest',
            'httpx',
            # other test dependencies
        ]
    },
    entry_points={
        'console_scripts': [
            'deepseek-init=app.utils.helpers:initialize_database'
        ]
    }
)
