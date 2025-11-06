"""
Stack Overflow Developer Survey Analysis Project
Setup script for the project
"""

from setuptools import setup, find_packages

# README dosyasını oku
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Requirements dosyasını oku
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="stack-overflow-survey-analysis",
    version="1.0.0",
    author="Data Scientist",
    author_email="data.scientist@example.com",
    description="A comprehensive analysis of Stack Overflow Developer Survey data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/stack-overflow-survey-project",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "jupyterlab>=3.4.0",
            "ipywidgets>=7.6.0",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

