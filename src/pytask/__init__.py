from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import pymysql


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/pytaskdb' --> OLD
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://root:root@db/pytaskdb') # --> NEW
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = False
app.secret_key = '3oXa26gmb4FrtrHQwsGBqBUs9Ht'

db = SQLAlchemy(app)


from pytask import routes