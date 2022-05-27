# This file is responsible for everything database
# Primarily the instantiation of our ORM and the creation of our database tables (models/entities)

# import our orm
from flask_sqlalchemy import SQLAlchemy
# create the instance of our ORM (object relational mapper)
db = SQLAlchemy()

# setup login manager
from flask_login import LoginManager, UserMixin
# create the instance of our LoginManager
login = LoginManager()

# tell our login manager how it can access a User object from a user_id
@login.user_loader
def load_user(userid):
    return User.query.get(userid)

# tools for our models
from datetime import datetime
from uuid import uuid4
from werkzeug.security import generate_password_hash

# create a DB model -> aka a Python object that will be a table/entity in our SQL database
class Animal(db.Model):
    # global attributes for each column in the database
    id = db.Column(db.String(40), primary_key=True) 
    species = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    latin_name = db.Column(db.String(255), default=None)
    size_cm = db.Column(db.Integer)
    diet = db.Column(db.String(255))
    lifespan = db.Column(db.String(255))    
    description = db.Column(db.String(255), nullable=False)    
    image = db.Column(db.String(250), default=None)
    price = db.Column(db.Float(2), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    
    def __init__(self, dict) -> None:
        super().__init__()
        self.id = str(uuid4())
        self.name = dict['name'].title()
        self.species = dict['species'].title()
        self.price = dict['price']
        self.description = dict['description']
        self.image = dict.get('image')
        self.size_cm = dict.get('size_cm',0)
        self.latin_name = dict.get('latin_name', 'unknown')[0].upper() + dict.get('latin_name', 'unknown')[1:].lower()
        self.diet = dict.get('diet', 'unknown')
        self.lifespan = dict.get('lifespan',0)

    def to_dict(self):
        return {
            'id': self.id,
            'species': self.species,
            'latin_name': self.latin_name,
            'image': self.image,
            'description': self.description,
            'price': self.price,
            'size_cm': self.size_cm,
            'diet': self.diet,
            'lifespan': self.lifespan,
            'created_on': self.created_on
        }
        
    def from_dict(self, dict):
        for k,v in dict.items():
            getattr(self,k)
            setattr(self,k,v)

# create our User model
class User(db.Model, UserMixin):
    id = db.Column(db.String(40), primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(255), default='No bio')
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=datetime.utcnow())
    api_token = db.Column(db.String(100))
    posts = db.relationship('Post', backref='post_author')

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body= db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    author = db.Column(db.String, db.ForeignKey('user.id'))