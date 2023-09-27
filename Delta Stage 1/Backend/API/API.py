#API

from flask import Flask, jsonify

counter = 0

app = Flask(__name__)
@app.route('/index')
def hello_world():
    global counter
    counter += 1
    response_data = {
        "message": "Hello World",
        "call_count": counter
    }
    return jsonify(response_data)

if __name__ == '__main__': 
   app.run()