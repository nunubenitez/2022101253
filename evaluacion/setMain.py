
from flask import Flask, jsonify, request
from setrest import setrest

app = Flask(__name__) 

##servicios rest
app.register_blueprint(setrest)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    ##app.run(host = '127.0.0.1', debug = True, port = 5000)
    app.run(host = '0.0.0.0', debug = True, port = 5000)
    app.run(debug = True)