import datetime
from sqlalchemy import Integer, String,ForeignKey, Column, Boolean
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Post(SqlAlchemyBase):
    __tablename__ = 'lapka'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    costs = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)

    def __repr__(self):
        return f'{self.id, self.title, self.text, self.costs, self.color, self.rating}'