from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, DateField, BooleanField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from myflask.models import User


class SignupForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[DataRequired()])
    last_name = StringField(label='Last Name', validators=[DataRequired()])
    email = EmailField(label='Email Address', validators=[DataRequired()])
    DOB = DateField(label='Date of Birth', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    password_repeat = PasswordField(label='Confirm Pass',
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    user_type = StringField(label="Account Type", validators=[DataRequired()])
    country = StringField(label='Country', validators=[DataRequired()])

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is not None:
            raise ValidationError('An account is already registered for that email address')


