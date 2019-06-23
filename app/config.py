"""
	Application configurations
"""
from typing import List
from flask import Flask
from flask_dotenv import DotEnv

class Config:
    """ Base configurations """
    DEBUG = False
    TESTING = False
    # SECRET_KEY = os.getenv('SECRET')
    @classmethod
    def init_app(cls, app: Flask, env_files: List):
        """ .env file load """
        env = DotEnv()
        for env_file in env_files:
            env.init_app(app, env_file=env_file, verbose_mode=cls.DEBUG)

class ProductionConfig(Config):
    """ production configurations """
    DEBUG = False

class DevelopmentConfig(Config):
    """ development configurations """
    DEBUG = True
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    """ test configurations """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    TESTING = True

CONFIG_BY_NAME = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
