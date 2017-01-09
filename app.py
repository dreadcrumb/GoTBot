
import json
import os

from distance_script import *

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)
#Trying stuff
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<name>")
def hello_name(name):
    return "Hello {}!".format(name)

#Actual app
@app.route("/webhook", methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))
    parameters = req.get("result").get("parameters")

    start = parameters["start"]
    end = parameters["end"]
    vehicle = parameters.get("vehicle", None)


    res = get_distance(start,end,vehicle)

    r = make_response(res)

    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == "__main__":
    app.run()




