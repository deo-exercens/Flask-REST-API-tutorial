"""
	Flask Controll script
"""
from flask_script import Manager

from app import create_app

APP = create_app('dev', env_files=[
    "./app/.env",
    "./confs/database/mysql/.env"
])

APP.app_context().push()

MANAGER = Manager(APP)

@MANAGER.command
def run():
    """ app running command """
    APP.run(
        host=APP.config['HOST'],
        port=APP.config['PORT'],
        debug=APP.config['DEBUG']
    )

@MANAGER.command
def test():
    """ app testing command """
    import pytest
    return pytest.main(['-vx', 'app/tests'])

if __name__ == '__main__':
    MANAGER.run()
