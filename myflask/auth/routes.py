from flask import Blueprint, render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError
from urllib.parse import urlparse, urljoin
from myflask import db, login_manager
from myflask.auth.forms import SignupForm, LoginForm, UpdateForm, ChangePassword, DeleteAccount
from myflask.models import User
from datetime import timedelta

auth_bp = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to view that page.', 'red-100')
    return redirect(url_for('auth.login'))


def is_safe_url(target):
    host_url = urlparse(request.host_url)
    redirect_url = urlparse(urljoin(request.host_url, target))
    return redirect_url.scheme in ('http', 'https') and host_url.netloc == redirect_url.netloc


def get_safe_redirect():
    url = request.args.get('next')
    if url and is_safe_url(url):
        return url
    url = request.referrer
    if url and is_safe_url(url):
        return url
    return '/'


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                    DOB=form.DOB.data, user_type=form.user_type.data, country=form.country.data,
                    username=form.username.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            login_user(user, duration=timedelta(minutes=1))
            if user.user_type == 'C':
                flash(f"Hello, {user.first_name}. You have successfully signed up.", 'green-100')
            else:
                flash(f"Hello, {user.first_name}. You have successfully signed up and your role as an administrator is pending approval", 'yellow-100')
        except IntegrityError:
            db.session.rollback()
            flash(f'Error, unable to register {form.email.data}. ', 'red-100')
            return redirect(url_for('auth.signup'))
        return redirect(url_for('main.index'))
    return render_template('signup.html', title='Sign Up', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        login_user(user, remember=login_form.remember.data, duration=timedelta(minutes=1))
        flash(f"Welcome back, {user.first_name}", 'blue-100')
        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)
        return redirect(next or url_for('main.index'))
    return render_template('login.html', title='Login', form=login_form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def update():
    form = UpdateForm(request.form, obj=current_user)
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        current_user.country = form.country.data
        try:
            db.session.commit()
            flash('Your profile has been successfully update', 'blue-100')
        except IntegrityError:
            db.session.rollback()
            flash(f'Error, the email {form.email.data} is associated with another account', 'red-100')
        return redirect(url_for('auth.update'))
    return render_template('update_profile.html', title='Your Profile', form=form)


@auth_bp.route('/settings/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePassword(obj=current_user)
    if form.validate_on_submit():
        current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('Your password has been updated', 'green-100')
        return redirect(url_for('auth.change_password'))
    return render_template('change_password.html', title='Change Password', form=form)


@auth_bp.route('/settings/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
    form = DeleteAccount(obj=current_user)
    if form.validate_on_submit():
        db.session.delete(current_user)
        db.session.commit()
        flash('Your account has been deleted', 'blue-100')
        return redirect(url_for('auth.login'))
    return render_template('delete_account.html', title='Delete Account', form=form)
