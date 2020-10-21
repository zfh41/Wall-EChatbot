# models.py
import flask_sqlalchemy
from app import db
from enum import Enum


class Usps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(400))
    url=db.Column(db.Integer)
    guser=db.Column(db.String(400))
    imgurl=db.Column(db.String(400))
    
    def __init__(self, a, url, guser, imgurl):
        self.address = a
        self.url=url
        self.guser=guser
        self.imgurl=imgurl
    def __repr__(self):
        return '<Usps address: %s>' % self.address 
        
        
class AuthUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auth_type = db.Column(db.String(120))
    name = db.Column(db.String(120))
    
    def __init__(self, name, auth_type):
        assert type(auth_type) is AuthUserType
        self.name = name
        self.auth_type = auth_type.value
        
    def __repr__(self):
        return "<User name: {}\ntype: {}".format(self.name, self.auth_type)

class AuthUserType(Enum):
    LINKEDIN = "linkedin"
    GOOGLE = "google"
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    TWITTER = "twitter"
    GITHUB = "github"
    PASSWORD = "password"

