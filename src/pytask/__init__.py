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

#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(80), unique=True, nullable=False)
#    password = db.Column(db.String(80), nullable=False)
#    projects = db.relationship('Project', backref='owner', lazy=True)
#
#class Project(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    title = db.Column(db.String(100), nullable=False)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#    todos = db.relationship('Todo', backref='project', lazy=True)
#
#class Todo(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    description = db.Column(db.String(200), nullable=False)
#    due_date = db.Column(db.DateTime, nullable=False)
#    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
#    is_completed = db.Column(db.Boolean, default=False, nullable=False)brav
