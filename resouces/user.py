import sqlite3
from flask_restful import Resource, reqparse
from model.user import UserModel

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

		if UserModel.find_by_username(project['username']):
			return {'message':'A user with this username is already exist'}, 400
		
		user = UserModel(**project)
		user.save_to_db()

		return {"Message": "User created successfully"}, 201











