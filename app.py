from flask import Flask, jsonify,request
import time
import json

app = Flask(__name__);
@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    res = query + " " + time.ctime()
    return jsonify({"response" : res})
if __name__=="__main__":
    app.run(threaded=True)
