from flask import Flask
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
csrf.exempt_views.add('dash.dash.dispatch')


def _protect_dash_views(dash_app):
    for view_func in dash_app.server.view_functions:
        if view_func.startswith(dash_app.config.routes_pathname_prefix):
            dash_app.server.view_functions[view_func] = login_required(dash_app.server.view_functions[view_func])


def register_dash_apps(app):
    with app.app_context():
        from mydash.layoutindex import DashAppIndex
        dash_app_index = DashAppIndex(app)
        dash_app_index.setup()
        _protect_dash_views(dash_app_index.app)

        from mydash.layout1 import DashApp1
        dash_app1 = DashApp1(app)
        dash_app1.setup()
        _protect_dash_views(dash_app1.app)

        from mydash.layout2 import DashApp2
        dash_app2 = DashApp2(app)
        dash_app2.setup()
        _protect_dash_views(dash_app2.app)

        from mydash.layout3 import DashApp3
        dash_app3 = DashApp3(app)
        dash_app3.setup()
        _protect_dash_views(dash_app3.app)

        from mydash.layout4 import DashApp4
        dash_app4 = DashApp4(app)
        dash_app4.setup()
        _protect_dash_views(dash_app4.app)


def create_app(config_class_name):
    app = Flask(__name__)
    app.config.from_object(config_class_name)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    csrf.init_app(app)

    register_dash_apps(app)

    with app.app_context():
        from myflask.models import User
        db.create_all()

    from myflask.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    from myflask.main.routes import main_bp
    app.register_blueprint(main_bp)

    return app
