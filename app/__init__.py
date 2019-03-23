# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.routes.search_route import api as search_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='SearchAPI',
          version='1.0.0',
          description='a rest api to search products'
          )

api.add_namespace(search_ns, path='/search')