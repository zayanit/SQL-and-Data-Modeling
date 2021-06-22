from flask import Flask, request, jsonify, abort
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zayan@127.0.0.1:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Todo(db.Model):
	__tablename__ = 'todos'
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(), nullable=False)

	def __repr__(self):
		return f'<TODO {self.id} {self.description}>'

# db.create_all()

@app.route('/')
def index():
	return render_template('index.html', data=Todo.query.all())

@app.route('/todos/create', methods=['post'])
def create_todo():
	error = False
	body = {}
	try:
		# description = request.form.get('description', '')
		description = request.get_json()['description']
		todo = Todo(description = description)
		db.session.add(todo)
		db.session.commit()
		body['description'] = todo.description
	except:
		error = True
		db.session.rollback()
		print(sys.exc_info())
	finally:
		db.session.close()
	if error:
		abort(400)
	else:
		# return redirect(url_for('index'))
		return jsonify(body)