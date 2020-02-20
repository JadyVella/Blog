import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = '9f32301b269c54d1d976c269d5a644'
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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://felixmoringa:#379JadyDady@localhost/blog1'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}