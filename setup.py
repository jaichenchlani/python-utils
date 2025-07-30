from setuptools import setup, find_packages

setup(
    name="jaiutils",
    version="1.0.0",
    author="Jai",
    description="Personal Python utilities for various projects",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)