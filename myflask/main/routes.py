from flask import Blueprint
from flask import render_template
from flask_login import login_required, UserMixin

main_bp = Blueprint('main', __name__, url_prefix='/')


@main_bp.route('/')
def welcome():
        return render_template('welcome.html', title="Welcome")


@main_bp.route('/home')
@login_required
def index():
    return render_template('index.html', title="Home")
