import os

class Config:
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	UPLOADED_PHOTOS_DEST ='app/static/photos'
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://aphya5:NewPasword@localhost/pitches'

    # email configurations
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

	@staticmethod
	def init_app(app):
		pass

class Config:
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class TestConfig(Config):
	'''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://aphya5:NewPasword@localhost/pitches'


class ProdConfig(Config):
	'''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
	'''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://aphya5:NewPasword@localhost/pitches'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
