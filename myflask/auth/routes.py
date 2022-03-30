from flask import Blueprint
from flask import render_template

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/')
def signup():
    return render_template('signup.html', title="Create Your Free Account")
