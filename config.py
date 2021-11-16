import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    # MAIL_USE_TLS = False
    MAIL_USERNAME = ''  # 接收邮箱地址
    MAIL_PASSWORD = '' # 授权码
    POSTS_PER_PAGE = 5
    LANGUAGES = ['en', 'zh']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
