from flask import Flask, render_template, request, url_for
from datetime import datetime
from os import path
import json

app = Flask(__name__)

message_list = []

max_messages = 30


def add_message(name, text):
    now = datetime.now()
    current_time = now.strftime('%H:%M')
    global message_list
    new_message = {
        "name": name,
        "text": text,
        "time": current_time,
    }
    message_list.append(new_message)
    if len(message_list) > max_messages:
        message_list = message_list[-max_messages:]


add_message('Irochka', 'Welcome guys')


# http://127.0.0.1:5000/send_message?name=Irochka&text=Hello
@app.route('/get_messages')
def get_messages():
    return {"messages": message_list}


@app.route('/send_message')
def send_message():
    name = request.args.get('name')
    text = request.args.get('text')

    if 12 < len(name) < 3:
        return {'result': False, 'error': 'Invalid name'}

    add_message(name, text)
    return 'OK'


@app.route('/chat')
def display_chat():
    return render_template('chat.html')


app.run()
