from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

	def get(self, name):
		store = StoreModel.find_by_name('name')
		if store:
			return store.json()
		return {'Message': 'Store not found'}, 404

	def post(self, name):
		if StoreModel.find_by_name('name'):
			return {'Message': 'Store {} is already exists'.format('name')}, 400

		store = StoreModel(name)
		try:
			store.save_to_db()
		except:
			return{'Message': 'An error has occured while creating a store'}, 500

		return store.json(), 201

	def delete(self, name):
		store = StoreModel.find_by_name('name')
		if store:
			store.delete_from_db()

		return {'Message': 'Store {} has been deleted'.format('name')}


class StoreList(Resource):
	def get(self):
		return {'store': [store.json() for store in StoreModel.query.all()]}