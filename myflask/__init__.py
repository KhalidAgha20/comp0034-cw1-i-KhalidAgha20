from flask import Flask
#from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
#login_manager = LoginManager()
csrf = CSRFProtect()


def create_app(config_class_name):
    app = Flask(__name__)
    app.config.from_object(config_class_name)

    db.init_app(app)
    #login_manager.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        from myflask.models import User
        db.create_all()


    from myflask.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    from myflask.main.routes import main_bp
    app.register_blueprint(main_bp)

    return app
