import time
from flask import Flask
from flask import request, redirect
from flask import make_response, render_template
from flask_login import UserMixin, LoginManager, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
import os
import bcrypt


app = Flask(__name__)

JWT_SECRET = os.getenv("JWT_SECRET")
app.config['SECRET_KEY'] = JWT_SECRET
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)
db = SQLAlchemy(app)

@login_manager.user_loader
def get_user():
    return User.query.all()

class User(db.Model, UserMixin):
    tablename = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(254))
    email = db.Column(db.String(254))
    salt = db.Column(db.String(254))
with app.app_context():
    db.create_all()
    db.session.commit()

def initApp():
	return app
