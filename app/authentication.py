from flask import Flask
from flask import request, redirect
from flask import make_response, render_template
from uuid  import uuid4
import bcrypt as bc
import databaseTool as dbt
from homepageLogic import generateSite
#hashed_password = b'$2b$12$YegDi5sS7DB4QCA9/XfEGu4P7VFgKs5qaXjUqW87QI9V2kv3qFJaC'
#authenticated_users = {"71991798-5b27-4e88-85a4-1beec1e6da58" : "bach"}

def authenticate(request):
  if request.method == "GET":
    return render_template("forms.html")
  
  username = request.form.get("username", "")
  password = request.form.get("password", "")
  hashed_password, correct_hash=dbt.getPassword(username,password)
  print(correct_hash)
  if bc.checkpw(bytes(password, "utf-8"), correct_hash):
    sid = str(uuid4())
    #authenticated_users[sid] = "admin"
    response = redirect("/", code=302)
    response.set_cookie("sid", sid)
    return generateSite()

  return "Wrong username or password", 400

def registerInDatabase(request):
	login = request.form.get("login", "")
	password = request.form.get("password", "")
	email_address = request.form.get("email", "")
	salt = bc.gensalt()
	hashed = bc.hashpw(bytes(password, "utf-8"),salt)
	dbt.putInDatabase(request, login, hashed, email_address, salt)
