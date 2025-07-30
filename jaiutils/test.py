from llm import query_gemini

prompt = "What is Kubernetes?"
response = query_gemini(prompt)
print(response)