# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal Python utilities package (`jaiutils`) containing reusable modules for various projects. This is a simple Python package using setuptools for distribution.

## Development Commands

### Installation
```bash
# Install in development mode
pip install -e ~/mydata/technical/personal/python-utils/
```

### Package Management
```bash
# Build package
python setup.py sdist bdist_wheel

# Install dependencies
pip install requests
```

## Code Architecture

- **Package structure**: Standard Python package with `setup.py` and single `jaiutils/` module directory
- **Current modules**:
  - `llm.py`: Gemini API interface with error handling and timeout configuration
- **Dependencies**: Minimal - only `requests` library required
- **Environment**: Requires `GEMINI_API_KEY` environment variable for LLM functionality

## Module Patterns

- Each utility module should be self-contained with clear function interfaces
- Use type hints for all function parameters and return values
- Include comprehensive error handling with descriptive error messages
- Follow snake_case naming convention for functions and variables
- New modules go directly in `jaiutils/` directory and can be imported as `from jaiutils import module_name`