"""
	Application configurations
"""
from typing import List
import os

from flask import Flask
from flask_dotenv import DotEnv

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
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].format(
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
CONFIG_BY_NAME = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

CONFIG_FILES_BY_NAME = dict(
    dev=[
        "/app/.env",
        "/confs/database/mysql/.env",
    ],
    test=[
        "/app/.env",
        "/confs/database/mysql/.env",
    ]
)
