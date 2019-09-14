# this is where we initialize the whole application
from flask import Flask
from flask_restful import Api
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to Uliza api"

# import routes
from app.routes.users import api_endpoint
from app.routes.posts import api_endpoint