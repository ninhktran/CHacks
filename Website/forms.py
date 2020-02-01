from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email

class RegistrationFrom(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    everett = BooleanField("Everett")
    skagit_county = BooleanField("Skagit County")
    weather = BooleanField("Weather")
    sports = BooleanField("Sports")
    submit = SubmitField('Submit')