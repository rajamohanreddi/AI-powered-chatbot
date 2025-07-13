from flask import Flask, request, render_template, jsonify
from chatbot import get_bot_response
from database import init_db, log_interaction

app = Flask(__name__)
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    bot_response = get_bot_response(user_input)
    log_interaction(user_input, bot_response)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
