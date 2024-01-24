from flask import Flask, jsonify, render_template, request
from chatbot_framework import chatbot

app = Flask(__name__)

chatbot = chatbot()


@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods = ["GET", "POST"])
def chat():
    msg = request.form.get('msg')
    user_query = msg
    chatbot.recieve_query(str(user_query))
    return get_answer()

def get_answer():
    chatbot.process_query()
    return chatbot.chatGPT()

if __name__ == '__main__':
    app.run()



