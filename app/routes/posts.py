from app import app
from flask import jsonify
from flask_restful import Api

# import controllers
from app.controllers.posts import Posts
from app.controllers.posts import Post

api_endpoint = Api(app)
api_endpoint.add_resource(Posts, '/api/posts')
api_endpoint.add_resource(Post, '/api/posts/<int:post_id>')