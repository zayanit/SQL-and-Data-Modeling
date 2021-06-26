from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, lazyload

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zayan@127.0.0.1:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Ecample: a driver has many vehicles
class Driver(db.Model):
  __tablename__ = 'drivers'
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  name = db.Column(db.String(), nullable=False)
  state = db.Column(db.String(5), nullable=True)
  issued = db.Column(db.DateTime)
  vehicles = db.relationship('Vehicle', backref='driver', lazy=True)

class Vehicle(db.Model):
  __tablename__ = 'vehicles'
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  make = db.Column(db.String(20), nullable=False)
  model = db.Column(db.String(20), nullable=False)
  year = db.Column(db.String(4), nullable=False)
  driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)
