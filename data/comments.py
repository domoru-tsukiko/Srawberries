import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Comment(SqlAlchemyBase):
    __tablename__ = 'comments'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    post_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("posts.id"))
    author_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("accounts.id"))
    text = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_answer = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    answer_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('comments.id'))

    author = orm.relation('Account')
    post = orm.relation('Post')
    answer = orm.relation('Comment')
