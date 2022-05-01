from pickle import TRUE
from flask import Flask

# Create a Flask instance 
app = Flask(__name__)

# Create a route decorater 
@app.route("/")

def index():
    return ''<h1>Hello World </h1>"





if __name__=="main":
    app.run(debug=True)