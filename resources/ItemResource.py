from flask_restful import Resource
from schemas import ItemSchema
from models import Item

class ItemResource(Resource):
    schema = ItemSchema()
    
    def get(self, itemId):
        item = Item.objects.get(id = itemId)
        result = self.schema.dump(item)
        return {'result': result}

class ItemsListResource(Resource):
    schema = ItemSchema(many = True)

    def get(self):
        items = Item.objects
        result = self.schema.dump(items)
        return {'result': result}