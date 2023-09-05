from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user
from flask_socketio import SocketIO
from datetime import datetime

from . import db
from .models import Message, User

chat = Blueprint('chat', __name__)
socketio: SocketIO = current_app.extensions['socketio']

@chat.route('/chat', methods=['GET', 'POST'])
@login_required
def home():
  messages = (Message.query
              .join(User, User.id == Message.owner)
              .add_columns(Message.content, Message.created_at, User.nickname)
              .all())

  return render_template('chat.html', user=current_user,
                       messages=messages)

@socketio.event
def send_message(data):
  content = data['msg']

  if content == '':
    return

  message = Message(content=content, owner=current_user.id, room=1)
  db.session.add(message)
  db.session.commit()

  sended_at = datetime.strftime(message.created_at, '%d/%m/%Y %H:%M')

  socketio.emit('recieve_message', {'user': current_user.nickname,
                                    'content': content,
                                    'sended_at': sended_at})
