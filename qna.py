from gemini_client import ask_gemini


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational assistant.
Answer the student's question accurately and concisely.
If useful, give a short explanation or example.

Question:
{question}
"""
    return ask_gemini(prompt)
