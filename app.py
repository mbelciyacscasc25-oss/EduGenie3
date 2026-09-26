from flask import Flask, render_template, request, jsonify, redirect
from dotenv import load_dotenv
from ai.gemini import ask_gemini
from ai.fallback import get_fallback_response

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("dashboard.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/subjects")
def subjects():
    return render_template("subjects.html")


@app.route("/ai-tutor")
def ai_tutor():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/progress")
def progress():
    return render_template("progress.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    question = (data.get("message") or "").strip()

    if not question:
        return jsonify({
            "success": False,
            "error": "Please enter a question."
        }), 400

    try:
        answer = ask_gemini(question)
        if answer:
            return jsonify({
                "success": True,
                "answer": answer,
                "source": "Gemini AI"
            })
    except Exception:
        pass

    answer = get_fallback_response(question)
    return jsonify({
        "success": True,
        "answer": answer,
        "source": "EduGenie Fallback"
    })

if __name__ == "__main__":
    app.run(debug=True)
