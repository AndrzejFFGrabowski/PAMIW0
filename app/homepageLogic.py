from flask import make_response, render_template
import requests
import json

uri = "http://127.0.0.1:5000/jsonrpc"
headers = {'content-type': 'application/json'}

def generateSite():
    return render_template("homepage.html")

def searchLogic():
	payload = {
        "method": "echo",
        "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
	r = requests.post(
		uri,data=json.dumps(payload), headers=headers).json()
	assert response["result"] == "echome!"
	assert response["jsonrpc"] == "2.0" 
	assert response["id"] == 0 
	return r
