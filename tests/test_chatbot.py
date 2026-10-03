import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "chatbot"))

os.environ.pop("OPENAI_API_KEY", None)
from app import app  # noqa: E402
from chatbot_engine import generate_reply  # noqa: E402


def test_home_page_loads():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"AI Assistant" in response.data


def test_chat_endpoint_returns_reply():
    response = app.test_client().post("/chat", json={"message": "hello"})
    assert response.status_code == 200
    assert "reply" in response.get_json()


def test_chat_endpoint_rejects_empty_message():
    response = app.test_client().post("/chat", json={"message": "  "})
    assert response.status_code == 400


def test_chat_endpoint_rejects_long_message():
    response = app.test_client().post("/chat", json={"message": "x" * 2001})
    assert response.status_code == 400


def test_offline_fallback_is_available():
    assert "Python" in generate_reply("python")
  
