import json
import flask
import flask_socketio

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/host')
def host():
    return flask.render_template(
        'host.html',
        host_room_id=flask.request.args.get('host_room_id'),
        player_room_id=flask.request.args.get('player_room_id')
    )


@app.route('/play')
def play():
    return flask.render_template(
        'play.html',
        host_room_id=flask.request.args.get('host_room_id'),
        player_room_id=flask.request.args.get('player_room_id')
    )


@socketio.on('join')
def join(data):
    socketio.join_room(data)


@socketio.on('query')
def query(data):
    socketio.emit('query', data, room=data['room'])


@socketio.on('answer')
def answer(data):
    socketio.emit('answer', data, room=data['room'])
