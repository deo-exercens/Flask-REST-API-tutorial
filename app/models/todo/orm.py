# pylint: disable=E1101
"""
	Todo ORM
"""
from sqlalchemy.sql import text

from app import DB

class Todo(DB.Model):
    """ Todo model """
    __tablename__ = "Todo"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = DB.Column("id", DB.Integer, primary_key=True)
    name = DB.Column("name", DB.String(250), nullable=False)
    done = DB.Column(DB.Boolean, nullable=False)
    created = DB.Column(DB.TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), nullable=False)

    def __init__(self, name, done, **kwargs):
        self.name = name
        self.done = done
        super(Todo, self).__init__(**kwargs)
