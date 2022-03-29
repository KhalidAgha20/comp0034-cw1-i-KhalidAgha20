from flask import Blueprint

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/auth')
def index():
    return "This is the authentication section of the web app"

