import os

# ----------FLASK-WTF扩展库配置--------- #
CSRF_ENABLED = True
SECRET_KEY = 'cbdc2869ed1d4aae90ce92a1a9053c90'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ----------FLASK-SQLALCHEMY数据库配置---------#
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
DB = 'datatest'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://%s:%s@%s/%s' % (USERNAME, PASSWORD, HOST, DB)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

