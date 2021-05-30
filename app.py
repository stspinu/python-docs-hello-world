from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    x = 1
    y = 2
    return f"Hello, everyone - {x+y}"

@app.route("/s")
def hi():
    x = 1
    y = 10
    return f"Hello, your number is - {x+y} this time."

