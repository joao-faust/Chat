from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  nickname = db.Column(db.String(20), unique=True, nullable=False)
  password = db.Column(db.String(150), nullable=False)
  created_at = db.Column(db.DateTime(timezone=True), default=func.now(),
                         nullable=False)

class Room(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False, unique=True)
  description = db.Column(db.String(200), nullable=False)
  owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  created_at = db.Column(db.DateTime(timezone=True), default=func.now(),
                         nullable=False)
  closed_at = db.Column(db.DateTime(timezone=True))

class Message(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(1000), nullable=False)
  owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  room = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
  created_at = db.Column(db.DateTime(timezone=True), default=func.now(),
                         nullable=False)
