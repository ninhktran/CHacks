from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegistrationFrom(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    everett = BooleanField("Everett")
    skagit_county = BooleanField("Skagit County")
    weather = BooleanField("Weather")
    sports = BooleanField("Sports")
