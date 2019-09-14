# users controllers
# this is where our businesss logic lies
from app import app
from flask import jsonify, request
from flask_restful import Resource
# from flask.ext.bcrypt import Bcrypt

# import models
from app.models.users import users_db
# remember users_db is a fuction in the models so we pass the returned values to users
users = users_db()


class Users(Resource):
    # get all users
    def get(self):
        return { 'users': users} ,200
    # post a user
    def post(self):
        users_data = {}
        data = request.get_json()
        users_data['id'] = len(users)+1
        users_data['firstname'] = data['firstname']
        users_data['lastname'] = data['lastname']
        users_data['email'] = data['email']
        users_data['password'] = data['password']
        users.append(users_data)
        return { 'users': users_data} ,201

class User(Resource):
    # get a specific user by id
    def get(self,id):
        user = [ user for user in users if user['id'] == id ]
        if user:
            return { 'user': user[0] } ,200
        else:
            return { 'message': 'The user you are looking is not found' } , 404
