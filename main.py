from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


""" I followed example videos from youtube channel Codemy.com :) """


# Create Flask instance.
app = Flask(__name__)
app.config['SECRET_KEY'] = "Python Key For Secret Bidness"

# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bands.db'
db = SQLAlchemy(app)



# Create a form class
class NameForm(FlaskForm):
    name = StringField("What da name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create route decorator.
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)


# Error Page
# Invalide URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


# Create Name Page
@app.route("/name", methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Thanks for submission!")
    return render_template("name.html",
        name = name,
        form = form)



if __name__ == "__main__":
    app.run()