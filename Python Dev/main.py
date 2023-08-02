from flask import Flask, render_template
from flask_socketio import SocketIO, send
import socket

# recebendo o endereço IP
hostname = socket.gethostname()
ipAdress = socket.gethostbyname(hostname)

# creação do aplicativo e do websocket
app = Flask(__name__)
socketIO = SocketIO(app, cors_allowed_origins="*")


@socketIO.on("message")
def sendMessage(message):
    send(message, broadcast=True)


@app.route("/")
def index():
    return render_template("index.html")


socketIO.run(app, host=ipAdress)