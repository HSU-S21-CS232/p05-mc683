from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


""" I followed example videos from youtube channel Codemy.com :) """


# Create Flask instance.
app = Flask(__name__)

# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bands.db'
db = SQLAlchemy(app)





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


if __name__ == "__main__":
    app.run()