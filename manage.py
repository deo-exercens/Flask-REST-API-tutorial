# pylint: disable=W0401, C0413, W0614
"""
	Flask Controll script
"""
import os
import sys

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app
from app import DB

APP = create_app(mode=os.getenv("ENV", "dev"))

DB.init_app(APP)

from app.models.todo.orm import *

APP.app_context().push()

MANAGER = Manager(APP)

MIGRATE = Migrate(APP, DB)

MANAGER.add_command('db', MigrateCommand)

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
    """
    application test code 실행 command
    $ python manage.py test
    """
    import pytest
    root_dir = APP.config['ROOT_DIR']
    test_path = '{ROOT_DIR}/app/tests'.format(ROOT_DIR=root_dir)
    coverage_option = '--cov-config={ROOT_DIR}/.coveragerc'.format(ROOT_DIR=root_dir)
    errno = pytest.main([test_path, coverage_option])
    sys.exit(errno)

if __name__ == '__main__':
    MANAGER.run()
