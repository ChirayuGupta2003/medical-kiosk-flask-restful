from flask import request, url_for, redirect
from .base_resource import BaseResource
import bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity, decode_token
from models.user import User
import datetime


class Login(BaseResource):

    def post(self):
        data = request.json

        email = data.get("email")
        password = data.get("password")


        user_document = User.objects(email=email).first()

        if user_document and bcrypt.checkpw(password.encode("utf-8"), user_document["password"].encode("utf-8")):
            access_token = create_access_token(
                identity={"email": email, "name": user_document["name"]}, expires_delta=datetime.timedelta(days=1))


            return {"token": access_token}

        return {"error": "Invalid username or password"}
