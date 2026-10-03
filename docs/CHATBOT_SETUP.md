# AI Chatbot Setup

This document explains how to install, configure, run, and test the AI-Powered Chatbot.

## Run locally

1. Unzip this pack into the **root of the existing repository**, merging folders when prompted. Do not delete existing files.
2. Create and activate a virtual environment:
   - Windows PowerShell: `py -m venv .venv` then `.venv\\Scripts\\Activate.ps1`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Start the server: `python chatbot/app.py`
5. Open `http://127.0.0.1:5000` in your browser.

The app runs in local FAQ mode without an API key, so you can test the interface without spending money. To enable OpenAI-generated answers, copy `.env.example` to `.env`, add your API key, and load the environment variables before starting the app. For example, install `python-dotenv` (included) and launch with:

```bash
python -c "from dotenv import load_dotenv; load_dotenv(); from chatbot.app import app; app.run(host='127.0.0.1', port=5000, debug=False)"
```

Never commit `.env` or share your API key. API usage may incur charges. Keep the server bound to `127.0.0.1` for local development; do not deploy the Flask development server directly to the public internet.

## Test

From the repository root, run `python -m pytest -q`.

## New files in this pack

- `chatbot/app.py` — Flask pages and `/chat` API endpoint
- `chatbot/chatbot_engine.py` — optional OpenAI integration and local FAQ fallback
- `chatbot/templates/index.html` and `chatbot/static/` — chat UI
- `requirements.txt` — dependencies for the new chatbot
- `.env.example` — names of optional environment variables, no secret values
- `.gitignore` — ignores local environments and secrets
- `tests/test_chatbot.py` — basic endpoint and fallback tests

These files are additions only. The repository's existing README, licence, contribution guide, applications, and GitHub workflow are intentionally not included in this ZIP.
