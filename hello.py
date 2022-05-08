from ast import Return
from pickle import TRUE
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField
from wtforms.validators import DataRequired

# Create a Flask instance 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Nsindiso'

class NamerForm(FlaskForm):
    name = StringField("Whats Your Name ? " ,validators=[DataRequired()])
    submit = SubmitField("Submit")


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

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form 
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html", name=name, form = form) 


if __name__=="main":
    app.run(debug=True)