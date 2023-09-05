from flask import (Blueprint, render_template, request,
                   redirect, url_for, flash)
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from flask_login import login_user, logout_user, current_user

from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    nickname = request.form.get('nickname')
    password = request.form.get('password')

    user = User.query.filter_by(nickname=nickname).first()

    if user and check_password_hash(user.password, password):
      flash('Login efetuado!', category='success')
      login_user(user, remember=True)
      return redirect(url_for('chat.home'))
    else:
      flash('Credenciais inválidas', category='error')
      return redirect(url_for('auth.login'))

  if current_user.is_authenticated:
    return redirect(url_for('chat.home'))

  return render_template('login.html')

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    data = request.form
    nickname = data.get('nickname')
    password_1 = data.get('password-2')
    password_2 = data.get('password-2')

    if User.query.filter(User.nickname == nickname).first():
      flash(message='Nickname já existe', category='error')
    elif len(nickname) < 1 or len(nickname) > 20:
      flash(message='Nickname inválido', category='error')
    elif len(password_1) < 8 or password_2 != password_1:
      flash(message='Senha inválida', category='error')
    else:
      user = User(nickname=nickname,
                  password=generate_password_hash(password_1, method='sha256'))
      db.session.add(user)
      db.session.commit()
      login_user(user, remember=True)
      flash('Conta criada!', category='success')
      return redirect(url_for('chat.home'))

  return render_template('sign_up.html')

@auth.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('auth.login'))
