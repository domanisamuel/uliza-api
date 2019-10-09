from app import app
from flask import jsonify
from flask_restful import Api

# import controllers
from app.controllers.users import Users
from app.controllers.users import User

api_endpoint = Api(app)
api_endpoint.add_resource(Users, '/api/v1/users')
api_endpoint.add_resource(User, '/api/v1/users/<int:user_id>')
