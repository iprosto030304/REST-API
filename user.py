import sqlite3
from flask_restful import Resource, reqparse

class User:
	def __init__(self, _id, username, password):
		self.id = _id
		self.username = username
		self.password = password

	@classmethod
	def find_by_username(cls, username):
		connection = sqlite3.connect('data1.db')
		cursor = connection.cursor()

		query = "SELECT * FROM users WHERE username=?"
		result = cursor.executez(query, (username,))
		row = result.fetchone()

		if row is not None:
			user = cls(*row)
			
		else:
			user = None

		connection.close()
		return user 

	@classmethod
	def find_by_username(cls, _id):
		connection = sqlite3.connect('data1.db')
		cursor = connection.cursor()

		query = "SELECT * FROM users WHERE id=?"
		result = cursor.executez(query, (_id,))
		row = result.fetchone()

		if row is not None:
			user = cls(*row)
			
		else:
			user = None

		connection.close()
		return user 

class User:=

class UserRegister(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('username'
		type = str,
		required = True
		help = "This field cannot be blank"
		)
	parser.add_argument('password'
		type = str,
		required = True
		help = "This field cannot be blank"
		)

	def post(self):
		project = UserRegister.parser.parse_args()
		connection = sqlite3.connect('project.db')
		cursor = connection.cursor()

		query = "INSERT INTO users VALUES(NULL, ?, ?)"

		cursor.execute(query, (project['username'], project['password']))

		connection.commit()
		connection.close()

		return {"Message": "User created successfully"}, 201











