import datetime
import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from . import db_session
from .db_session import SqlAlchemyBase
from flask_login import UserMixin, current_user

from .likes import Like
from .posts import Post
from .comments import Comment


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

    def count_like(self):
        db_sess = db_session.create_session()
        posts = db_sess.query(Post.count_likes).filter(Post.author_id == current_user.id).all()
        a = []
        for post in posts:
            a.append(post[0])
        return sum(a)

    def count_comm(self):
        db_sess = db_session.create_session()
        posts = db_sess.query(Post.count_comments).filter(Post.author_id == current_user.id)
        a = []
        for post in posts:
            a.append(post[0])
        return sum(a)

    def count_my_comm(self):
        db_sess = db_session.create_session()
        comms = db_sess.query(Comment).filter(Comment.author_id == current_user.id).all()
        return len(comms)

    # def tap_like(self, post):
    #     db_sess = db_session.create_session()
    #     if current_user.id not in db_sess.query(Like.author_id).filter(Like.post_id == post.id):
    #         post.count_likes += 1
    #         db_sess.add(Like(author_id=current_user.id, post_id=post.id))
    #         db_sess.commit()
