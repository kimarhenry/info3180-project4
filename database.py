from flask import Flask
from passlib.apps import custom_app_context as pwd_context
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '//postgres:620068542@localhost/wishlist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

class Userinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    

    def __init__(self,username,password):
        self.username = username
        self.password=password
       
    def __repr__(self):
        return '<User %r>' % self.username



class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wishurl=db.Column(db.String(1000), unique=False)
    href=db.Column(db.String(150), unique=False)
    date=db.Column(db.String(100), unique=False)
    user_id=db.Column(db.Integer, db.ForeignKey("userinfo.id"))
    category=db.Column(db.String(100), unique=False)
    quantity=db.Column(db.String(100), unique=False)
    description=db.Column(db.String(100), unique=False)


    def __init__(self,wishurl,href,date,user_id,category,quantity,description):
        self.wishurl=wishurl
        self.href=href
        self.date=date
        self.user_id=user_id
        self.category=category
        self.quantity=quantity
        self.description=description



