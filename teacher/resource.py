from flask_restful import Resource


class Teacher(Resource):

    def post(self):
        return {'message': 'Post method'}

    def get(self, id=None):
        return {'message': 'get method'}

    def put(self, id=None):
        return {'message': 'Put method'}

    def delete(self, id=None):
        return {'message': 'delete method'}
