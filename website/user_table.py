#!/usr/bin/python3
"""Create the user, role, roles_users tables"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin

app = Flask(__name__)

app.config['SECRET_KEY'] ='Secret_key_to_be_generated'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin_pwd@localhost/club_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECURITY_PASSWORD_SALT'] = 'Secret_salt_to_be_generated'

db = SQLAlchemy(app)

roles_users = db.Table('roles_users', 
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('user.id')), 
                       db.Column('role_id', db.Integer(), 
                                 db.ForeignKey('role.id'))
                       )

class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    fs_uniquifier = db.Column(db.String(255), unique=True)
    roles = db.relationship('Role',
                            secondary=roles_users, 
                            backref=db.backref('users', lazy='dynamic')
                            )

class Role(RoleMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

with app.app_context():
   db.create_all()
   user_datastore.create_role(name='admin')
