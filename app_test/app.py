from flask import Flask

app = Flask(__name__)

@app.route("/baby")
def hello():
    return "Hello, World!"