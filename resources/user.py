from .base_resource import BaseResource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User as UserModel
import json


class User(BaseResource):

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()

        user = UserModel.objects(email=current_user).first()

        user = json.loads(user.to_json())

        # for idx, obj in enumerate(user):
        #     print(idx, obj)

        del user["password"]
        del user["_id"]
        
        return {"user": user}
