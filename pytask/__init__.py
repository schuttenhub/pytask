from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/pytaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    projects = db.relationship('Project', backref='owner', lazy=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    todos = db.relationship('Todo', backref='project', lazy=True)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)



from pytask import routes