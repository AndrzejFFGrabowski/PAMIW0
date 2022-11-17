import time
from signalLogic import generateSignalSite
from flask import Flask
from flask import request, redirect
from flask import make_response, render_template
from uuid  import uuid4
from bcrypt import checkpw
from authentication import authenticated_users, authenticate
from homepageLogic import generateSite, searchLogic
from dotenv import load_dotenv
from os import getenv
from redis import StrictRedis

load_dotenv(verbose=True)

JWT_SECRET = getenv("JWT_SECRET")
SECRET_CREDENTIALS=getenv("SECRET_CREDENTIALS")

redis_url = "redis://127.0.0.1"
app = Flask(__name__)
app.config["REDIS_URL"] = redis_url
#db = StrictRedis.from_url(redis_url, decode_responses=True)
try:
  db.echo("ping")
except:
  print("ERROR communicating with Redis database.")
  print("Start Redis instance first. Exiting.")
  exit(1)

from flask import url_for
from flask_sse import sse
app.register_blueprint(sse, url_prefix="/stream")

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

@app.route("/signal", methods=["GET", "POST"])
def generateSignal():
    return generateSignalSite()

#if __name__ == '__main__':
#    app.run(host="192.168.1.122", port=5050)
