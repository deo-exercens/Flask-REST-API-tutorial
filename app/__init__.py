"""
	flask REST API application
"""
from typing import List
from flask import Flask

from app.config import CONFIG_BY_NAME

def create_app(config_name: str, env_files: List)-> (Flask):
    """ flask app factory """
    app = Flask(__name__)
    config = CONFIG_BY_NAME[config_name]
    config.init_app(app, env_files=env_files)
    app.config.from_object(config)
    return app
