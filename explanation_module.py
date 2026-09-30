from transformers import pipeline

# Lightweight local explanation model described in the project document.
MODEL_NAME = "MBZUAI/LaMini-Flan-T5-783M"

_generator = None


def _get_generator():
    global _generator
    if _generator is None:
        _generator = pipeline(
            "text2text-generation",
            model=MODEL_NAME
        )
    return _generator


def explain_topic(topic: str) -> str:
    prompt = (
        "Explain the following topic in simple language for a beginner. "
        "Use short paragraphs and simple examples.\n\n"
        f"Topic: {topic}"
    )

    try:
        generator = _get_generator()
        result = generator(prompt, max_new_tokens=250, do_sample=False)
        return result[0]["generated_text"]
    except Exception as exc:
        return f"Explanation module error: {exc}"
