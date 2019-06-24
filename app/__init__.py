"""
	flask REST API application
"""
from typing import List
from flask import Flask

from app.config import CONFIG_BY_NAME
from app.config import CONFIG_FILES_BY_NAME

def create_app(mode: str)-> (Flask):
    """ flask app factory """
    app = Flask(__name__)
    config = CONFIG_BY_NAME[mode]
    env_files = CONFIG_FILES_BY_NAME[mode]
    config.init_app(app, env_files=env_files)
    app.config.from_object(config)
    return app
