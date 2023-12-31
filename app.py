import os
from dotenv import load_dotenv

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

import mongoengine

from resources.home import Home
from resources.login import Login
from resources.register import Register
from resources.protected import Protected
from resources.user import User

load_dotenv()

app = Flask(__name__)
CORS(app)
api = Api(app, prefix="/api")


api.add_resource(Home, "/", endpoint="home")
api.add_resource(Login, "/login", endpoint="login")
api.add_resource(Register, "/register", endpoint="register")
api.add_resource(Protected, "/protected", endpoint="protected")
api.add_resource(User, "/user", endpoint="user")


def set_mongo_client():
    # start = time.time()

    # client = pymongo.MongoClient(os.getenv("MONGO_URI"))
    # db = client.dev

    # app.config["MONGO_CLIENT"] = client
    # app.config["MONGO_DB"] = db

    # end = time.time()
    # print(f"Connected to db!, time taken: {round(end-start, 3)} sec")

    mongoengine.connect(host=os.getenv("MONGO_URI"))


def set_up_jwt():
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
    jwt = JWTManager(app)


set_mongo_client()
set_up_jwt()
