from flask_socketio import SocketIO

from src import create_app

app = create_app()

if __name__ == '__main__':
  socketio: SocketIO = app.extensions['socketio']
  socketio.run(app)
