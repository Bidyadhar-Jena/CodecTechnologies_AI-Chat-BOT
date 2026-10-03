"""Reply engine with a no-key FAQ fallback and optional OpenAI integration."""
import os

FAQS = {
    "hello": "Hi! 👋 I'm your AI assistant. Ask me about this project, Python, or how to get started.",
    "hi": "Hey there! What can I help you with?",
    "help": "I can answer basic questions about Python, this project, and getting started. Set OPENAI_API_KEY in your environment for AI-generated replies.",
    "project": "This is a Flask-based chatbot demo. It has a browser chat interface, a reply API, and an optional OpenAI integration.",
    "python": "Python is a readable, general-purpose programming language used in web development, automation, data science, and AI.",
    "install": "From the repository root, run: python -m venv .venv, activate it, then run pip install -r requirements.txt. Start the app with python chatbot/app.py.",
    "contact": "This demo has no contact database configured yet. Add your approved support details to the FAQ data before using it for customer support.",
    "bye": "Goodbye! 👋 Come back whenever you need help.",
}

SYSTEM_PROMPT = (
    "You are a friendly, concise support chatbot for a beginner Python project. "
    "Answer clearly, do not claim to access private systems, and say when you do not know."
)


def _faq_reply(message: str) -> str:
    text = message.lower().strip()
    # Exact/word matching keeps the fallback predictable and useful without an API key.
    for keyword, answer in FAQS.items():
        if text == keyword or keyword in text.split():
            return answer
    if any(word in text for word in ("thank", "thanks")):
        return "You're welcome! 😊"
    return (
        "I'm running in offline FAQ mode, so I may not understand that yet. "
        "Try asking about Python, this project, installation, or help. "
        "For broader AI replies, configure OPENAI_API_KEY in your environment."
    )


def generate_reply(message: str) -> str:
    """Generate a reply. Uses OpenAI when configured; otherwise uses local FAQs."""
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        return _faq_reply(message)

    # Import lazily so the app still works in FAQ mode if the SDK is unavailable.
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message},
            ],
            max_tokens=300,
            temperature=0.5,
        )
        content = response.choices[0].message.content
        return content.strip() if content else _faq_reply(message)
    except Exception:
        # Keep the demo usable if the key/model/network is misconfigured.
        return _faq_reply(message)
