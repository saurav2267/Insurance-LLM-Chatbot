# llm/local_llm.py

import subprocess

def generate_response(context: str, user_query: str) -> str:
    """
    Calls Mistral via Ollama CLI with context and query as input.
    Returns the generated response.
    """
    prompt = f"""You are an intelligent assistant for insurance analysts.

Use the following information to answer the question as clearly and concisely as possible.

Context:
{context}

Question:
{user_query}

Answer:"""

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=60  # seconds
        )
        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        return "LLM timed out. Try a shorter question."
    except Exception as e:
        return f"Error generating response: {e}"
