from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zayan@127.0.0.1:5432/flaskdemodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<User ID: {self.id}, Name: {self.name}>'

db.create_all()


# Queries which I run in the terminal

# from demo2Query import User, db
# user = User(name='Bob')
# db.session.add(user)
# db.session.commit()

### Transient: an object exists, it was defined
# user1 = User(name='Mohammed')  ## Transient Stage
# user2 = User(name='Fawzy')     ## Transient Stage
# user3 = User(name='Ahmed')     ## Transient Stage

# db.session.add_all([user1, user2, user3])   ## Stage Pending
# db.session.commit()

# the same result for filtering
# User.query.filter(User.name=='Bob').all()
# db.session.query(User).filter_by(name='Bob').all()

# User.query.filter(User.name.like('%d%')).all()
# User.query.filter(User.name.like('%d%')).limit(5).all()
# User.query.filter(User.name.like('%M%')).all()
# User.query.filter(User.name=='Bob').count()