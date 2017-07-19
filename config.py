import os

DEBUG = True

SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL', 'mysql+pymysql://blogz2:MyNewPass@localhost:8889/blogz2')
SQLALCHEMY_ECHO = True

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'
