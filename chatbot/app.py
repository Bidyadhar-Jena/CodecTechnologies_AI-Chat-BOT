load_dotenv()

API_KEY = os.getenv("API_KEY")

"""Small Flask web app for an AI-powered FAQ chatbot."""
from flask import Flask, jsonify, render_template, request
from chatbot_engine import generate_reply

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024  # 16 KB request limit


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "Please enter a message."}), 400
    if len(message) > 2000:
        return jsonify({"error": "Message must be 2,000 characters or fewer."}), 400
    try:
        reply = generate_reply(message.strip())
        return jsonify({"reply": reply})
    except Exception:
        app.logger.exception("Chat reply generation failed")
        return jsonify({"error": "Sorry, something went wrong. Please try again."}), 500


if __name__ == "__main__":
    # Debug is intentionally off by default. Do not expose the dev server publicly.
    app.run(host="127.0.0.1", port=5000, debug=False)
  
