import flask_login._compat
import sqlalchemy
from flask_login import UserMixin
from mytools.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):

    user_id = db.Column('id', db.Integer, primary_key=True)
    password_hash = db.Column(db.String(200))
    username = db.Column(db.String(100))
    # 用户最近一次登陆时间
    lastseen = db.Column(db.DateTime, default=sqlalchemy.func.now())

    __tablename__ = 'tb_user'

    def __init__(self, user_id=None, password=None, username="anonymous"):
        self.user_id = user_id
        self.password_hash = password
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return flask_login._compat.unicode(self.user_id)

    def set_password(self, raw_password):
        """密码加密"""
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        """校验密码是否正确"""
        return check_password_hash(self.password_hash, raw_password)

    def __repr__(self):
        return '<User {user}>'.format(user=self.username)
