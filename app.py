import json
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv, find_dotenv

# Load env first so anything imported afterwards sees the vars
load_dotenv(find_dotenv())

from generator import generate_content  # now it's safe to import

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/generate", methods=["POST"])
def api_generate():
    data = request.get_json(force=True)
    topic = (data.get("topic") or "").strip()
    content_type = (data.get("contentType") or "").strip()

    if not topic or content_type not in {"flashcards", "quiz", "study_guide", "outline"}:
        return jsonify({"error": "Please provide a topic and a valid content type."}), 400

    try:
        result_json_str = generate_content(topic, content_type)
        result = json.loads(result_json_str)  # validate JSON
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY not set. Check your .env file.")
    app.run(debug=True)

