"""
	Application configurations
"""
from typing import List
import os

from flask import Flask
from flask_dotenv import DotEnv

from app.constants import SQLALCHEMY_DATABASE_URI

class Config:
    """ Base configurations """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def init_app(cls, app: Flask, env_files: List):
        """ .env file load """
        env = DotEnv()
        config_py_path = os.path.realpath(__file__)
        app_path = os.path.dirname(config_py_path)
        project_root_path = os.path.dirname(app_path)
        app.config['ROOT_DIR'] = project_root_path
        for env_file in env_files:
            env_file = project_root_path + env_file
            env.init_app(app, env_file=env_file, verbose_mode=cls.DEBUG)
        env.eval(keys={
            "MYSQL_PORT": int,
            "PORT": int,
        })
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI.format(
            USER=app.config['MYSQL_DATABASE_USERNAME'],
            PASSWORD=app.config['MYSQL_ROOT_PASSWORD'],
            ADDR=app.config['MYSQL_DATABASE_HOST'],
            PORT=app.config['MYSQL_PORT'],
            NAME=app.config['MYSQL_DATABASE']
        )

class ProductionConfig(Config):
    """
        Production 설정
        환경변수는 systemd의 Service section에서 EnvironmentFile으로 불러옴
    """
    ENV = "production"
    DEBUG = False

class DevelopmentConfig(Config):
    """
        Development 설정
    """
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    """
        Testing 설정
        기본적으로 단위 테스트를 수행
        기능 및 통합 테스트 시 환경변수에 설정이 안되어 있을 경우 에러 발생
    """
    ENV = "testing"
    TESTING = True
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ContinuousIntegrationConfig:
    """
        지속적 통합을 위한 설정
        .env 파일은 SCM에 없으므로
        환경변수를 이용하여 설정값을 등록하도록 수정
    """
    ENV = "ci"
    TESTING = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # application variable
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    LOG_PATH = os.getenv('LOG_PATH')
    SECRET_KEY = os.getenv('SECRET_KEY')

    # database variable
    MYSQL_DATABASE_USERNAME = os.getenv('MYSQL_DATABASE_USERNAME')
    MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
    MYSQL_DATABASE_HOST = os.getenv('MYSQL_DATABASE_HOST')
    MYSQL_PORT = os.getenv('MYSQL_PORT')

    SQLALCHEMY_DATABASE_URI.format(
        USER=MYSQL_DATABASE_USERNAME,
        PASSWORD=MYSQL_ROOT_PASSWORD,
        ADDR=MYSQL_DATABASE_HOST,
        PORT=MYSQL_PORT,
        NAME=MYSQL_DATABASE,
    )
    @classmethod
    def init_app(cls, app: Flask, env_files: List):
        """ duck method """
        _ = app, env_files
        config_py_path = os.path.realpath(__file__)
        app_path = os.path.dirname(config_py_path)
        project_root_path = os.path.dirname(app_path)
        cls.ROOT_DIR = project_root_path

CONFIG_BY_NAME = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig,
    ci=ContinuousIntegrationConfig
)

CONFIG_FILES_BY_NAME = dict(
    dev=[
        "/app/.env",
        "/confs/database/mysql/.env",
    ],
    test=[
        "/app/.env",
        "/confs/database/mysql/.env",
    ],
    prod=[],
    ci=[]
)
