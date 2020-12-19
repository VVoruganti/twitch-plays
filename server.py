from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@socketio.on('connection')
def handle_connection(socket):
    print(socket)


if __name__ == 'main':
    socketio.run(app)
    
