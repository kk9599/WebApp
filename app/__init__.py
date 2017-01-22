from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail


import os
basedir = os.path.abspath(os.path.dirname("__file__"))

db = SQLAlchemy()
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    #init the app setting

    app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    #
    # if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
    #     from flask_sslify import SSLify
    #     sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')



    return app