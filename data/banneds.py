import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Ban(SqlAlchemyBase):
    __tablename__ = 'banneds'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    account_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('accounts.id'))
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)

    account = orm.relation('Account')
