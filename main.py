from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from datetime import datetime


""" I followed example videos from youtube channel Codemy.com :) """


# Create Flask instance.
app = Flask(__name__)
app.config['SECRET_KEY'] = "Python Key For Secret Bidness"

# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bands.db'
db = SQLAlchemy(app)

# Db Model
class Bands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band = db.Column(db.String(50), nullable=False)
    year_formed = db.Column(db.Integer, nullable=False)

    # Create string
    def __repr__(self):
        return '<Name %r> self.name'


# Create band form Class
class BandForm(FlaskForm):
    band = StringField("Band Name", validators=[DataRequired()])
    year_formed = IntegerField("Year Formed", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a form class
class NameForm(FlaskForm):
    name = StringField("What da name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create route decorator.
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bands")
def bands():
    myBands = Bands.query.all()
    return render_template("bands.html", myBands=myBands)

@app.route("/band/add", methods=['GET', 'POST'])
def add_band():
    band = None
    year = 0
    form = BandForm()
    if form.validate_on_submit():
        band = Bands.query.filter_by(band=form.band.data).first()
        if band is None:
            band = Bands(band=form.band.data, year_formed=form.year_formed.data)
            db.session.add(band)
            db.session.commit()
        band = form.band.data
        form.band.data = ''
        form.year_formed.data = ''
        flash("Band Added!")
    our_bands = Bands.query.order_by(Bands.year_formed)
    return render_template("add_band.html",
        form=form,
        band=band,
        our_bands=our_bands)

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