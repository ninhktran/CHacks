from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError
from Website.models import Subscriber

class RegistrationFrom(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    everett = BooleanField("Everett")
    lake_stevens = BooleanField('Lake Stevens')
    snohomish_county = BooleanField('Snohomish County')

    weather = BooleanField("Weather")
    sports = BooleanField("Sports")
    events = BooleanField('Events')
    traffic = BooleanField('Traffic')
    emergency = BooleanField('Emergency')
    submit = SubmitField('Submit')

    def validate_email(self, email):
        subscriber = Subscriber.query.filter_by(email=email.data).first()
        if subscriber:
            raise ValidationError(
                'That email is taken. Please choose another one.')

class UnSubscribeForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    are_you_sure = BooleanField('Are you sure you want to unsubscribe?')
    submit = SubmitField('Submit')

    def validate_email(self, email):
        subscriber = Subscriber.query.filter_by(email=email.data).first()
        if not subscriber:
            raise ValidationError(
                'That email is not in our system.')