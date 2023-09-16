from .base_resource import BaseResource
from flask import request
from flask_jwt_extended import create_access_token
import bcrypt
from models.user import User, Medication
import datetime


class Register(BaseResource):

    def post(self):

        data = request.json

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        # dob = data.get("dob")
        # phone = data.get("phone")
        # gender = data.get("gender")
        # medications = data.get("medications")

        # if dob:
        #     dob = datetime.datetime.strptime(dob, "%d/%M/%Y")

        if not (name or email or password):
            return {"error": "name, email and password required"}, 400

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt())

        # user = User(name=name, email=email,
        #             password=hashed_password.decode("utf-8"), dob=dob, phone=phone, gender=gender)

        user = User(name=name, email=email,
                    password=hashed_password.decode("utf-8"))

        # if medications:
        #     print(medications)
        #     for medication in medications:
        #         user.medications.append(Medication(
        #             name=medication["name"], time=medication["time"], duration=medication["duration"]))

        if not email or not password:
            return {"error": "email and password required"}, 400

        if User.objects(email=email).first():
            return {"error": "email already exists"}, 400

        access_token = create_access_token(
            identity={"email": email, "name": name}, expires_delta=datetime.timedelta(days=1))

        user.save()

        return {"token": access_token}
