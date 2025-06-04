import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Post(SqlAlchemyBase):
    __tablename__ = 'lapka'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    costs = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    is_moderated = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    color = sqlalchemy.Column(sqlalchemy.String, nullable=False)
