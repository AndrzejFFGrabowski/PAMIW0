import time
from flask import Flask
from flask import request, redirect
from flask import make_response, render_template
from uuid  import uuid4
from bcrypt import checkpw
from authentication import authenticated_users, authenticate
from homepageLogic import generateSite, searchLogic
from sqlLogic import generateSqlSite, fuc, addProductToDB, showProducts
from dotenv import load_dotenv
from os import getenv

load_dotenv(verbose=True)

JWT_SECRET = getenv("JWT_SECRET")
SECRET_CREDENTIALS=getenv("SECRET_CREDENTIALS")

app = Flask(__name__,template_folder='./templates',static_folder='./static')


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

@app.route("/sql", methods=["GET"])
def generateSql():
    return generateSqlSite()

@app.route('/with-json', methods=["POST"])
def with_json():
    data = request.get_json(silent=True)
    if data:
    	ID = data.get("id","nothing")
    	name = data.get("product", "nothing")
    	addProductToDB()
    	return "", 200
    else:
    	ID = request.form.get("id","nothing")
    	name = request.form.get("product","nothing")
    	addProductToDB()
    	return "",200
    
    
@app.route("/showProducts", methods=["GET"])
def showProductsList():
    return showProducts()    
#if __name__ == '__main__':
#    app.run(host="192.168.1.122", port=5050)
