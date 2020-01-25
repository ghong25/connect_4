# main flask app

from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit, send

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {}      # dictionary of active rooms

@app.route('/')
def index():
    """
    index HTML
    """
    return render_template('static/index.html')
