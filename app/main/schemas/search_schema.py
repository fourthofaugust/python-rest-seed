from flask_restplus import Namespace, fields


class SearchSchema:
    api = Namespace('search', description='search opetaions')
    search = api.model('search', {
        'product_name': fields.String(required=True, description='name of the product')
    })