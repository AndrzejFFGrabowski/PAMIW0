from flask import make_response, render_template
import requests
import json

uri = "http://192.168.1.121:8080/jsonrpc"
headers = {'content-type': 'application/json'}

def generateSite():
    return render_template("homepage.html")

def searchLogic(request):
	A = request.form.get("A", "")
	B = request.form.get("B", "")
	payload = {
        "method": "mul",
        "params": [A , B],
        "jsonrpc": "2.0",
        "id": 1,
    }
	r = requests.post(
		uri,data=json.dumps(payload), headers=headers).json()
	return r


	
