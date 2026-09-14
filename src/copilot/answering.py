def answer(question: str) -> str:
    """Placeholder answer engine. Real retrieval arrives in week 3."""
    cleaned = question.strip()
    if not cleaned:
        return "Please ask a question."
    return f"I don't know yet, but you asked: {cleaned}"