import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Post(SqlAlchemyBase):
    __tablename__ = 'posts'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    topic_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("topics.id"))
    author_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("accounts.id"))
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    img_path = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    count_likes = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    count_comments = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_moderated = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

    author = orm.relation('Account')
    topic = orm.relation('Topic')
    like = orm.relation('Like', back_populates='post')

    def __repr__(self):
        return f'{self.id, self.topic_id, self.author_id, self.title, self.text, self.img_path, self.count_likes, self.count_comments, self.created_date, self.is_moderated}'
