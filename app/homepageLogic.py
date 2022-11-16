from flask import make_response, render_template

def generateSite():
    return render_template("homepage.html")

def searchLogic():
    return "yes"