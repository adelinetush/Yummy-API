from app.models import BaseModel
from app.models import db
from app import app
from flask_sqlalchemy import SQLAlchemy
import datetime 
from passlib.apps import custom_app_context as pwd_context

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)



class Category(BaseModel, db.Model):
    __tablename__ = "Category"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    name = db.Column(db.String(120))
    description = db.Column(db.String(500))

    def __init__(self, email, name, description):
        self.email = email;
        self.name = name
        self.description = description


    def serialize(self):
            return {
            'id':self.id,
            'email':self.email,
            'name':self.name,
            'description':self.description
    }

class Recipe(BaseModel,db.Model):
    __tablename__ = "Recipe"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Integer);
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    description = db.Column(db.Text());
    ingredients = db.Column(db.Text())

    def __init__(self, category, name, email, description, ingredients):
        self.category = category
        self.name = name
        self.email = email
        self.description = description
        self.ingredients = ingredients
    
    def serialize(self):
            return {
            'id':self.id,
            'email':self.email,
            'name':self.name,
            'description':self.description,
            'ingredients':self.ingredients
    }

class User(BaseModel,db.Model):
    '''base initizialization function'''
    __tablename__ = "User"

    id  = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(32),index=True)
    password = db.Column(db.String(128))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email;
        self.password_hash  = password
        self.password = password

    def __str__(self):
            return "User(id='%s')" % self.id

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
        return self.password_hash

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    def serialize(self):
            return {
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'password':self.password
            }

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user
    