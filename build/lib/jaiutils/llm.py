import os
import requests
import json
import time
from typing import Optional

# Configuration constants
API_KEY = os.environ.get('GEMINI_API_KEY')
# GEMINI_MODEL = "gemini-1.5-flash-latest"
GEMINI_MODEL = "gemini-2.5-pro-preview-05-06"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"


def query_gemini(prompt: str, max_retries: int = 3, timeout: int = 60) -> str:
    """
    Query Gemini API with a given prompt, including retry logic for network errors.
    
    Args:
        prompt (str): The prompt to send to Gemini API
        max_retries (int): Maximum number of retry attempts (default: 3)
        timeout (int): Request timeout in seconds (default: 60)
        
    Returns:
        str: Response text or error message
    """
    if not API_KEY:
        return "LLM unavailable: GEMINI_API_KEY not set"
    
    url = f"{BASE_URL}/{GEMINI_MODEL}:generateContent?key={API_KEY}"
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=timeout)
            
            if response.status_code == 200:
                result = response.json()
                response_text = result['candidates'][0]['content']['parts'][0]['text']
                return response_text.strip()
            else:
                return f"LLM error: API returned status {response.status_code}"
                
        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                time.sleep(wait_time)
                continue
            return f"LLM unavailable: Request timed out after {max_retries} attempts"
            
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                time.sleep(wait_time)
                continue
            return f"LLM unavailable: Network error after {max_retries} attempts - {str(e)}"
            
        except KeyError as e:      
            return f"LLM error: Unexpected API response format - {str(e)}"
        except Exception as e:
            return f"LLM error: {str(e)}"
    
    return "LLM unavailable: Max retries exceeded"