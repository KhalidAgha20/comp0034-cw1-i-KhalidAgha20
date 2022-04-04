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
    user_type = StringField(label="Account Type", validators=[DataRequired(message='Select an Account Type')])
    country = StringField(label='Country', validators=[DataRequired()])

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is not None:
            raise ValidationError('An account is already registered for that email address')


class LoginForm(FlaskForm):
    email = EmailField(label='Email address', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember = BooleanField(label='Remember me')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('No account found with that email address.')

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        if user is None:
            raise ValidationError('No account found with that email address.')
        if not user.check_password(password.data):
            raise ValidationError('Incorrect password.')
