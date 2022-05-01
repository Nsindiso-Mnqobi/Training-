from pickle import TRUE
from flask import Flask, render_template

# Create a Flask instance 
app = Flask(__name__)

# Create a route decorater 
@app.route("/")

def index():
    return  render_template("index.html")

@app.route("/user/<name>")

def user(name):
    return f"<h1>Hello {name}</h1>"


if __name__=="main":
    app.run(debug=True)