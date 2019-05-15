from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel



class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price'
    		type=float,
    		required=True
    		help='This field cannot be left blank!'

    		)
	parser.add_argument('store_id'
    		type=int,
    		required=True
    		help='Every item needs a store id'

    		)
	@jwt_required()
	def get(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			return item.json()
		else:
			return ('Message':'Item not  found'), 404
#		item = next(filter(lambda x: x['name'] == name, item), None)
#		for item in items:
#			if item['name'] == name:
#				return item
#		return{'item': item}, 200 if item is not None else 404 

	
	def post(self, name):
		if ItemModel.find_by_name(name):
			return{'Message': 'An item "{}" is already exists'.format(name)}, 400

		data = Item.parser.parse_args()
#		data = request.get_json()
		item = ItemModel(name, data['price'], data['store_id'])
		
		try:
		   item.save_to_db()
		except:
			return{'message':'An error has occured'}, 500

		return item.json(), 201 
    
    
	def delete(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			item.delete_from_db()

		return{'Message':'Item has been deleted'}

    def put(self, name):
    	data = Item.parser.parse_args()
#    	data = request.get_json()
    	item = ItemModel.find_by_name(name)
    	    	
    	if item is None:
    		item = ItemModel.find_by_name(name, data['price'], data['store_id'])
    	else:
    		item.price = data['price']
	   	
    	item.save_to_db()

    	return item.json()


class ItemList(Resource):
	def get(self):
		return {'item': [item.json() for item in ItemModel.query.all()]}