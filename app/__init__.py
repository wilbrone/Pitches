from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
# from flask_uploads import UploadSet,configure_uploads,IMAGES

from config import config_options


bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
# photos = UploadSet('photos',IMAGES)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

simple = SimpleMDE()

def create_app(config_name):
    app = Flask(__name__)

    # creating app configurations
    app.config.from_object(config_options[config_name])

    # initializing flask extentions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # registering BluePrint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # configure UploadSet
    # configure_uploads(app,photos)

    return app
