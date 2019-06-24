"""
	flask REST API application
"""
from typing import List
import os
import logging
from logging.config import dictConfig

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import CONFIG_BY_NAME
from app.config import CONFIG_FILES_BY_NAME

DB = SQLAlchemy()

def create_app(mode: str)-> (Flask):
    """ flask app factory """
    app = Flask(__name__)
    config = CONFIG_BY_NAME[mode]
    env_files = CONFIG_FILES_BY_NAME[mode]
    config.init_app(app, env_files=env_files)
    app.config.from_object(config)
    if 'TRAVIS_CI' not in os.environ:
        # https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
        dictConfig({
            'version':1,
            'formatters': {
                'default': {
                    'format': '[%(asctime)s] [%(levelname)s] [%(module)s:%(lineno)d]\n %(message)s',
                },
            },
            'handlers': {
                'file_handler': {
                    'class': 'logging.FileHandler',
                    'filename': app.config['LOG_PATH'] + '/app.log',
                    'formatter': 'default',
                },
                'console':{
                    'class':'logging.StreamHandler',
                    'formatter':'default',
                    'stream':'ext://sys.stdout',
                },
            },
            'root': {
                'level': 'INFO',
                'handlers': ['file_handler', 'console']
            }
        })

    return app
