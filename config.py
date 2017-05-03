# -*- coding: utf-8 -*-

"""
    my-flask-example.config
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Author: Y.Z.Y
    
"""


class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True