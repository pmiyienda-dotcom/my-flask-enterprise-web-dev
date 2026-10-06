from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def name():
    return "<h1> Hi, I am Pauline Moraa from Enterprise Web Dev!</h1>"