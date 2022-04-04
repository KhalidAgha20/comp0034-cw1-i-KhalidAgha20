from flask import Blueprint
from flask import render_template

main_bp = Blueprint('main', __name__,url_prefix='/')

@main_bp.route('/')
def welcome():
    return render_template('welcome.html', title="Welcome")

@main_bp.route('/home')
def index():
    return render_template('index.html', title="Home")
