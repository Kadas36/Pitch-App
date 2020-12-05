import os

class Config:

class prodConfig(config):
    pass

class DevConfig(config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}         