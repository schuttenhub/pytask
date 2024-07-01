from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import pymysql
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf import CSRFProtect

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/pytaskdb' --> OLD
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://root:root@db/pytaskdb') # --> NEW
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = False
app.secret_key = '3oXa26gmb4FrtrHQwsGBqBUs9Ht'

db = SQLAlchemy(app)

csrf = CSRFProtect(app)

pytask_limiter = Limiter(
    app = app,
    key_func = get_remote_address,
    default_limits = ["100 per day", "60 per hour"]
)

from pytask import routes