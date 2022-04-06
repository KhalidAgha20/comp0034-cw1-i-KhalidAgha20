from flask import Blueprint, redirect, url_for
from flask import render_template
from flask_login import login_required, UserMixin, current_user

main_bp = Blueprint('main', __name__, url_prefix='/')


@main_bp.route('/')
def welcome():
    if current_user.is_anonymous:
        return render_template('welcome.html', title="Welcome")
    return redirect(url_for('main.index'))


@main_bp.route('/home')
@login_required
def index():
    return render_template('index.html', title="Home")


@main_bp.route('/data/eruption_numbers')
@login_required
def eruption_numbers():
    return render_template('eruption_numbers.html', title="Number of Volcanic Eruptions")


@main_bp.route('/data/yearly_data')
@login_required
def yearly_data():
    return render_template('yearly_data.html', title="Yearly Data")


@main_bp.route('/data/for_countries')
@login_required
def for_countries():
    return render_template('for_countries.html', title="Data for Countries")


@main_bp.route('/data/population')
@login_required
def population():
    return render_template('population.html', title="Population Risk")


@main_bp.route('/dash_app_index')
@login_required
def dash_app_index():
    return redirect('/dash_app_index/')


@main_bp.route('/dash_app1')
@login_required
def dash_app1():
    return redirect('/dash_app1/')


@main_bp.route('/dash_app2')
@login_required
def dash_app2():
    return redirect('/dash_app2/')


@main_bp.route('/dash_app3')
@login_required
def dash_app3():
    return redirect('/dash_app3/')


@main_bp.route('/dash_app4')
@login_required
def dash_app4():
    return redirect('/dash_app4/')
