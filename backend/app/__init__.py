from flask import Flask

from config import config
from .database import db
from .routes import jwt, auth_bp


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    
    with app.app_context():
        jwt.init_app(app)
        db.init_app(app)
        db.create_all()

    from .routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

