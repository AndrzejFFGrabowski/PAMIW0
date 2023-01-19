import time
from flask import Flask
from flask import request, redirect
from flask import make_response, render_template
from uuid  import uuid4
from bcrypt import checkpw
from authentication import authenticated_users, authenticate, registerInDatabase
from homepageLogic import generateSite, searchLogic
from flask_login import UserMixin, LoginManager, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
import os
import bcrypt
from startup import initApp

app=initApp()

@app.route('/', methods=["GET"])
def index():
    #return render_template("forms.html")
    sid = request.cookies.get("sid")
    if sid in authenticated_users:
        return generateSite()
    return redirect("/authenticate", code=302)

@app.route("/authenticate", methods=["GET", "POST"])
def authenticateUser():
    return authenticate(request)

@app.route('/with-url/<argument>', methods=["GET"])
def with_url(argument):
    return "Got argument [" + argument + "]", 200

@app.route("/search", methods=["GET", "POST"])
def search():
	word = get_user(1).username
	print(word)
	return word
    #return searchLogic()

#database


@app.route("/register", methods=["GET", "POST"])
def register():
    registerInDatabase(request)
    return redirect("/authenticate")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
