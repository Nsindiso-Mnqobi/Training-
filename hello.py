from pickle import TRUE
from flask import Flask, render_template

# Create a Flask instance 
app = Flask(__name__)

# Create a route decorater 
@app.route("/")

def index():
    firstname = "Nsindiso"
    test = "This is <strong>bold</strong> text"
    certs = ["devnet", "CCNA", "CCNP", 45 ]
    return  render_template("index.html", name=firstname, test=test, certs=certs) 

@app.route("/user/<name>")

def user(name):
    return  render_template("user.html", username= name)

# Invalid URL
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

# Internale Server Error
@app.errorhandler(500)

def page_not_found(e):
    return render_template("500.html"), 500


if __name__=="main":
    app.run(debug=True)