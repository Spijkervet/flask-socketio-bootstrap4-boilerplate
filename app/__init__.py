'''
Boilerplate Python3 Flask SocketIO app

Janne Spijkervet, 2017
'''

import time, sys, json
from datetime import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

__version__ = '1.0.0'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def get_server_data():
    data = {}
    data["version"] = sys.version
    data["time"] = datetime.now().strftime("%m/%d/%Y, %I:%M:%S%p")
    return data

def send_data():
    data = get_server_data()
    emit("update", json.dumps(data), json=True)

@socketio.on('connected')
def connection_handler(data):
    pong(data)

@socketio.on('ping')
def pong(data):
    send_data()
    emit("pong")

def create_app(host):
    socketio.run(app, host, debug=True)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')
