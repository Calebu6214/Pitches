from flask import Flask
from flask_bootstrap import Bootstrap
from wtforms.fields import simple
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_simplemde import SimpleMDE
# from app import index
from flask_mail import Mail,Message
# from app import index # <-- See note below.



login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# Instatiating
bootstrap = Bootstrap()
db = SQLAlchemy()

photos = UploadSet('photos', IMAGES)
mail = Mail()

def create_app(config_name):
    '''
    Function that creates a instance of the app on run
    Args:
        config_name: configuration setting (development,production or test)
    '''
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # configure UploadSet...
    configure_uploads(app, photos)
    
    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
    
    return app