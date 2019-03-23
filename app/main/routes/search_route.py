from ..services.search_service import search_product

from flask import request
from flask_restplus import Resource

from ..schemas.search_schema import SearchSchema

api = SearchSchema.api
_search = SearchSchema.search

@api.route('/')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('search product by picture')
    @api.marshal_with(_search)
    def post(self):
        payload = request.json
        return search_product(payload)