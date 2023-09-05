from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_socketio import SocketIO

db = SQLAlchemy()

ENV = dotenv_values('.env')
DB_PATH = ENV['DB_PATH']
SECRET_KEY = ENV['SECRET_KEY']

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = SECRET_KEY
  app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH
  db.init_app(app)

  socketio = SocketIO(app, cors_allowed_origins='*')

  with app.app_context():
    from .auth import auth
    from .chat import chat

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(chat, url_prefix='/')

    from .models import User, Message, Room
    Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message= 'Faça o login para acessar esta página.'
    login_manager.login_message_category = 'error'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
