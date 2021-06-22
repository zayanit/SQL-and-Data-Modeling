from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zayan@127.0.0.1:5432/flaskdemodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)

  def __repr__(self):
    return f'<Person ID: {self.id}, Name: {self.name}>'

db.create_all()

@app.route('/')
def index():
  person = Person.query.first()
  return 'Hello ' + person.name + '!!'

# Alternative approach to run a Flask app: using __main__
'''
if __name__ == '__main__':
  app.run()
'''