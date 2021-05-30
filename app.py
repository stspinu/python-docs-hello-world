from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    x = 1
    y = 2
    return f"Hello, everyone - {x+y}"
