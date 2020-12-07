import os

class Config:
    
   '''
   General configuration parent class
   '''
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kadas36@localhost/pitches'
   SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kadas36@localhost/pitches'
   DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}         