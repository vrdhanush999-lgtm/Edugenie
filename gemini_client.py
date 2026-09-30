import os

try:
    import google.generativeai as genai
except ImportError:
    genai = None


API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

if genai and API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)
else:
    model = None


def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return plain text."""
    if model is None:
        return (
            "Gemini is not configured. Set GEMINI_API_KEY as an environment "
            "variable before using AI features."
        )

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as exc:
        return f"Gemini API error: {exc}"
