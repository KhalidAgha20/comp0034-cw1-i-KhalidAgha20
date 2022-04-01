from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, DateField, BooleanField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from myflask.models import User


class SignupForm(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired()])
    last_name = StringField(label='Last name', validators=[DataRequired()])
    email = EmailField(label='Email address', validators=[DataRequired()])
    DOB = DateField(label='Date of Birth', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    password_repeat = PasswordField(label='Repeat Password',
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    user_type = BooleanField(label="Account Type", validators=[DataRequired()])

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is not None:
            raise ValidationError('An account is already registered for that email address')


