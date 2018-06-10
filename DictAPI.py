from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__, static_url_path="")
api = Api(app)

attractions = {}

attractions_fields = {
    'id': fields.Integer,
    'attraction': fields.String,
    'age': fields.Integer,
    'price': fields.Float,
    'duration': fields.Integer
}


class Attraction(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        self.reqparse.add_argument('attraction', type=str, location='json')
        self.reqparse.add_argument('age', type=str, location='json')
        self.reqparse.add_argument('price', type=float, location='json')
        self.reqparse.add_argument('duration', type=int, location='json')
        super(Attraction, self).__init__()  # super().__init__() / attraction.__init__(self)

    @app.route('/attractions')
    def put(self):
        args = self.reqparse.parse_args()
        attraction = {
            'id': args['id'],
            'attraction': args['attraction'],
            'age': args['age'],
            'price': args['price'],
            'duration': args['duration']
        }
        attractions.update(attraction)
        return marshal(attraction, attractions_fields), 201

    @app.route('/attractions')
    def post(self):
        args = self.reqparse.parse_args()
        attraction = [attraction for attraction in attractions if attractions.get('id') == args['id']]
        if len(attraction) == 0:
            abort(404)
        attractions.pop(attraction[0])
        new_attraction = {
            'id': args['id'],
            'attraction': args['attraction'],
            'age': args['age'],
            'price': args['price'],
            'duration': args['duration']
        }
        attractions.update(new_attraction)
        return marshal(new_attraction, attractions_fields)

    @app.route('/attractions/<int:id>')
    def get(self, id):
        attraction = [attraction for attraction in attractions if attractions.get('id') == id]
        if len(attraction) == 0:
            abort(404)
        return marshal(attraction[0], attractions_fields)

    @app.route('/attractions/<int:id>')
    def delete(self, id):
        attraction = [attraction for attraction in attractions if attractions.get('id') == id]
        if len(attraction) == 0:
            abort(404)
        attractions.pop(attraction[0])
        return {'result': True}


api.add_resource(Attraction, '/attractions', endpoint='attractions')
api.add_resource(Attraction, '/attractions/<int:id>', endpoint='attraction')

if __name__ == '__main__':
    app.run(debug=True)
