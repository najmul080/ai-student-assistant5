import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

STUDENT_NAME = "Islam MD Najmul"
STUDENT_ID = "2026512841"

def get_ai_response(prompt):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "API key is not configured. Please add GEMINI_API_KEY in Render Environment Variables."

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=(
                "You are a helpful student AI assistant. "
                "Give a clear, simple answer in English. "
                "Keep the answer suitable for a university student. "
                f"Student question: {prompt}"
            ),
        )
        return response.text
    except Exception as e:
        return f"AI request failed: {e}"

@app.route("/")
def home():
    return render_template(
        "index.html",
        student_name=STUDENT_NAME,
        student_id=STUDENT_ID
    )

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    prompt = (data.get("prompt") or "").strip()

    if not prompt:
        return jsonify({"answer": "Please enter a question."}), 400

    answer = get_ai_response(prompt)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
