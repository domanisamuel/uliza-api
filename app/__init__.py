from flask import Flask
from flask_restful import Api
app = Flask(__name__)

# import routes
from app.routes.users import api_endpoint
