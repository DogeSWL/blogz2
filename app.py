from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI']  = os.environ.get('DATABASE_URL', 'mysql+pymysql://blogz2:MyNewPass@localhost:8889/blogz2')
app.config['SQLALCHEMY_ECHO'] = True

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'

db = SQLAlchemy(app)
