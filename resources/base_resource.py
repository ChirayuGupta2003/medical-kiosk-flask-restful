from flask import current_app
from flask_restful import Resource
from pymongo.database import Database
from pymongo.mongo_client import MongoClient
import datetime
import jwt
import os
import bcrypt


class BaseResource(Resource):
    def __init__(self):
        super().__init__()
        # self.mongo_client: MongoClient = current_app.config['MONGO_CLIENT']
        # self.db: Database = current_app.config['MONGO_DB']
