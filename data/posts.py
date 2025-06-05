import datetime
from sqlalchemy import Integer, String,ForeignKey, Column, Boolean
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Post(SqlAlchemyBase):
    __tablename__ = 'lapka'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_author = Column(Integer,ForeignKey("user.id",ondelete='CASCADE'))
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    costs = Column(Integer, nullable=False)
