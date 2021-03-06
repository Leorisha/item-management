from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found.'}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': 'A store with name {} already exists.'.format(name)}, 404

        store = StoreModel(name)
        try:
            store.upsert()
        except:
            return {'message': 'An error occurred while creating the store.'}, 404

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()

        return {'message': 'Store deleted.'}


class StoreList(Resource):

    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
