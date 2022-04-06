from flask_wtf import FlaskForm
from numpy.ma import count
from wtforms import StringField, PasswordField, EmailField, DateField, BooleanField
from wtforms.validators import DataRequired, EqualTo, ValidationError, length
from flask_login import current_user
from myflask.models import User


class SignupForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[DataRequired()])
    last_name = StringField(label='Last Name', validators=[DataRequired()])
    email = EmailField(label='Email Address', validators=[DataRequired()])
    DOB = DateField(label='Date of Birth', validators=[DataRequired()])
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    password_repeat = PasswordField(label='Confirm Pass',
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    user_type = StringField(label="Account Type", validators=[DataRequired(message='Select an Account Type')])
    country = StringField(label='Country', validators=[DataRequired()])

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is not None:
            raise ValidationError('An account is already registered for that email address')

    def validate_username(self, username):
        users = User.query.filter_by(username=username.data).first()
        if users is not None:
            raise ValidationError('The username is already taken')

    def validate_password(self, password):
        if len(password.data) < 8:
            raise ValidationError('Make sure your password is at least 8 characters')


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember = BooleanField(label='Remember Me')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('No account found with that username')

    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if user is None:
            return None
        if not user.check_password(password.data):
            raise ValidationError('Incorrect password.')


class UpdateForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[DataRequired()])
    last_name = StringField(label='Last Name', validators=[DataRequired()])
    email = EmailField(label='Email Address', validators=[DataRequired()])
    country = StringField(label='Country', validators=[DataRequired()])

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data)
        if count(users) > 1:
            raise ValidationError('An account is already registered for that email address')


class ChangePassword(FlaskForm):
    password = PasswordField(label='Old Password', validators=[DataRequired()])
    new_password = PasswordField(label='New Password', validators=[DataRequired()])
    repeat_password = PasswordField(
        label='Confirm Pass', validators=[DataRequired(), EqualTo('new_password', message='Passwords must match')])

    def validate_password(self, password):
        if not current_user.check_password(password.data):
            raise ValidationError('Incorrect password.')

    def validate_new_password(self, new_password):
        if len(new_password.data) < 8:
            raise ValidationError('Make sure your password is at least 8 characters')


class DeleteAccount(FlaskForm):
    password = PasswordField(label='Password', validators=[DataRequired()])

    def validate_password(self, password):
        if not current_user.check_password(password.data):
            raise ValidationError('Incorrect password.')
