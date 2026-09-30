from gemini_client import ask_gemini


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational passage.
Keep the important information, remove unnecessary repetition,
and use simple language suitable for quick revision.

Passage:
{text}
"""
    return ask_gemini(prompt)
