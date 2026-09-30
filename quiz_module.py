import json
import re
from gemini_client import ask_gemini


def clean_json_block(text: str) -> str:
    """Remove Markdown code fences around JSON."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_quiz(passage: str):
    prompt = f"""
Create exactly 3 multiple-choice questions from the passage below.

Return ONLY valid JSON in this format:
[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "correct_answer": "A"
  }}
]

Requirements:
- Exactly 3 questions.
- Exactly 4 options for each question.
- One correct answer per question.
- Questions must be based on the passage.
- Do not add Markdown or explanations outside the JSON.

Passage:
{passage}
"""

    raw = ask_gemini(prompt)

    try:
        cleaned = clean_json_block(raw)
        return {"quiz": json.loads(cleaned)}
    except Exception as exc:
        return {
            "error": f"Could not parse quiz JSON: {exc}",
            "raw_response": raw
        }
