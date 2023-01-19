from flask import Flask
from flask import request, redirect
from flask import make_response, render_template
from uuid  import uuid4
from bcrypt import checkpw
import databaseTool as dbt

hashed_password = b'$2b$12$YegDi5sS7DB4QCA9/XfEGu4P7VFgKs5qaXjUqW87QI9V2kv3qFJaC'
authenticated_users = {"71991798-5b27-4e88-85a4-1beec1e6da58" : "bach"}

def authenticate(request):
  if request.method == "GET":
    return render_template("forms.html")
  
  username = request.form.get("username", "")
  print(dbt.getPassword(username))
  password = request.form.get("password", "")
  if username == "admin" and checkpw(bytes(password, "utf-8"), hashed_password):
    sid = str(uuid4())

    authenticated_users[sid] = "admin"
    response = redirect("/", code=302)
    response.set_cookie("sid", sid)
    return response

  return "Wrong username or password", 400

def registerInDatabase(request):
	dbt.putInDatabase(request)
