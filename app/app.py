import time
from flask import Flask
from flask import request, redirect
from flask import make_response, render_template
from uuid  import uuid4
from bcrypt import checkpw
from authentication import authenticated_users, authenticate
from homepageLogic import generateSite, searchLogic
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
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/', methods=["GET"])
def index():
    #return render_template("forms.html")
    sid = request.cookies.get("sid")
    if sid in authenticated_users:
        return generateSite()
    return redirect("/authenticate", code=302)

@app.route("/authenticate", methods=["GET", "POST"])
def authenticateUser():
    return authenticate()

@app.route('/with-url/<argument>', methods=["GET"])
def with_url(argument):
    return "Got argument [" + argument + "]", 200

@app.route("/search", methods=["GET", "POST"])
def search():
    return searchLogic()

#database

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db = SQLAlchemy(app)

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


@app.route("/register", methods=["GET", "POST"])
def register():
    login = request.form.get("login", "")
    password = request.form.get("password", "")
    rpassword = request.form.get("rpassword", "")
    email_address = request.form.get("email", "")

    if request.method == 'POST':
        #hashed_password  = bcrypt.hashpw(password,"a")
        user_to_register = User(
                               username = login,
                               password = password,
                               email = email_address,
                               salt = "a"
                              )

        db.session.add(user_to_register)
        db.session.commit()
        return redirect("/authenticate")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
