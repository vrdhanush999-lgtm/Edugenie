from gemini_client import ask_gemini


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for the topic below.

Organize it from beginner to advanced level.
For each stage include:
1. Topics to learn
2. A suggested timeline
3. Practice suggestions
4. Useful resource types such as videos, articles, or books

Adapt the plan for a learner who is starting from the basics.

Topic:
{topic}
"""
    return ask_gemini(prompt)
