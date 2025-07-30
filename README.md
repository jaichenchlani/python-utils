# Jai's Personal Python Utilities

A collection of reusable Python modules for various projects.

## Installation

Install in development mode:
```bash
pip install -e ~/mydata/technical/personal/python-utils/
```

## Modules

### llm.py
Generic LLM interface for Gemini API calls.

**Usage:**
```python
from jaiutils import llm

response = llm.query_gemini("Your prompt here")
```

**Requirements:**
- Set `GEMINI_API_KEY` environment variable

## Adding New Modules

1. Add new `.py` files to the `jaiutils/` directory
2. Update `setup.py` if new dependencies are needed
3. Import in your projects: `from jaiutils import module_name`