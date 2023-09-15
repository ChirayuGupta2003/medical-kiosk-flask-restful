from .base_resource import BaseResource
from flask_jwt_extended import jwt_required, get_jwt_identity


class Protected(BaseResource):

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {"message": "Protected", "current_user": current_user}
