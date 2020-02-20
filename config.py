import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'fello'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://felixmoringa:#379JadyDady@localhost/blog1'

class ProdConfig(Config):
    '''
    Production configuration child class
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development configuration child class
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}