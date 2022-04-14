import datetime
import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class Account(SqlAlchemyBase, UserMixin):
    __tablename__ = 'accounts'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img_path = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_moderator = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    is_email_true = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

    posts = orm.relation('Post', back_populates='author')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
