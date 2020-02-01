from flask import render_template, url_for
from Website import app
from Website.forms import RegistrationFrom

@app.route("/")
def home():
    form = RegistrationFrom()
    return render_template("home.html", form=form)