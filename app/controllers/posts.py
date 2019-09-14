# posts controllers
# this is where our businesss logic lies
from app import app
from flask import jsonify, request
from flask_restful import Resource

# import models
from app.models.posts import posts_db
# remember posts_db is a fuction in the models so we pass the returned values to posts
posts = posts_db()


class Posts(Resource):
    # get all posts
    def get(self):
        return { 'posts': posts} ,200
    # add a post
    def post(self):
        posts_data = {}
        data = request.get_json()
        posts_data['post_id'] = len(posts)+1
        posts_data['tag'] = data['tag']
        posts_data['content'] = data['content']
        posts.append(posts_data)
        return { 'posts': posts_data} ,201

class Post(Resource):
    # get a specific post by post_id
    def get(self,post_id):
        post = [ post for post in posts if post['post_id'] == post_id ]
        if post:
            return { 'post': post[0] } ,200
        else:
            return { 'message': 'The post you are looking is not found' } , 404

    # edit a post
    def put(self,post_id):
        post = [ post for post in posts if post['post_id'] == post_id ]
        if post:
            data = request.get_json()
            post[0]['tag'] = data['tag']
            post[0]['content'] = data['content']
            return { 'modified post:': post[0] } ,200
        else:
            return { 'message': 'post did not update' } ,404

    # delete a post
    def delete(self,post_id):
        post = [ post for post in posts if post['post_id'] == post_id ]
        if post:
            del posts[0]
            return { 'message:': posts } ,204
        else :
            return { 'message': 'delete not successful' } ,404
