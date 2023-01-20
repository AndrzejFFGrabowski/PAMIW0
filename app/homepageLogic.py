from flask import make_response, render_template
import requests
import json

uri = "http://192.168.1.121:8080/jsonrpc"
headers = {'content-type': 'application/json'}

def generateSite():
    return render_template("homepage.html")

def searchLogic():
	payload = {
        "method": "add",
        "params": [1, 2],
        "jsonrpc": "2.0",
        "id": 1,
    }
	r = requests.post(
		uri,data=json.dumps(payload), headers=headers).json()
	assert r["result"] == 3
	assert r["jsonrpc"] == "2.0" 
	assert r["id"] == 1 
	return r


	
