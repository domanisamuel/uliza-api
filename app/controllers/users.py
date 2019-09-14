# users controllers
# this is where our businesss logic lies
from app import app
from flask import jsonify
from flask_restful import Resource

# import models
from app.models.users import users_db
# remember users_db is a fuction in the models so we pass the returned values to users
users = users_db()


class User(Resource):
    # get all users
    def get(self):
        return jsonify({ 'users': users})
    