from flask import Flask, request, render_template
from chatbot import generate_response
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])

def chatbot():
    user_input= request.form["message"]
    bot_response = generate_response(user_input)
    return bot_response

if __name__ == "__main__":
    app.run(debug=True)
