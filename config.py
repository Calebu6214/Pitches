import os
import secrets


class Config:
    '''
    General configuaration parent class
    '''
    SECRET_KEY = 'caleb'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "calebkimutai97@gmail.com"
    MAIL_PASSWORD = "Caleb254"
      #simple mde configurations 
    SIMPLEMDE_JS_IIFE=True
    SIMPLEMDE_USE_CDN=True

class ProdConfig(Config):
    '''
    Production configuration child class
    Args: 
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_CALEB")

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/pitches'
    DEBUG = True

class TestConfig(Config):
    '''
    Test configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/pitchlist_test'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
}