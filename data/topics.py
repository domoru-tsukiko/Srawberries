import datetime
import sqlalchemy

from .db_session import SqlAlchemyBase


class Topic(SqlAlchemyBase):
    __tablename__ = 'topics'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    img_path = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_moderated = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
