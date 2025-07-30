import os
import requests
import json

# Configuration constants
API_KEY = os.environ.get('GEMINI_API_KEY')
GEMINI_MODEL = "gemini-1.5-flash-latest"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"


def query_gemini(prompt: str) -> str:
    """
    Query Gemini API with a given prompt.
    
    Args:
        prompt (str): The prompt to send to Gemini API
        
    Returns:
        str: Response text or error message
    """
    try:
        if not API_KEY:
            return "LLM unavailable: GEMINI_API_KEY not set"
        
        # Gemini API endpoint
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
        
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            response_text = result['candidates'][0]['content']['parts'][0]['text']
            return response_text.strip()
        else:
            return f"LLM error: API returned status {response.status_code}"
            
    except requests.exceptions.RequestException as e:
        return f"LLM unavailable: Network error - {str(e)}"
    except KeyError as e:
        return f"LLM error: Unexpected API response format - {str(e)}"
    except Exception as e:
        return f"LLM error: {str(e)}"