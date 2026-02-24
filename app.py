from openai import OpenAI
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

load_dotenv()

client = OpenAI(api_key=os.getenv(
    "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"))
BOT_NAME = "Shadow_AI"


@app.route("/")
def home():
    return render_template("index.html")

# Chat route


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are {BOT_NAME}, a friendly AI chatbot."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})


if __name__ == "__main__":
    # Important: tell Flask to listen on all interfaces
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are {BOT_NAME}, a friendly AI chatbot."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
