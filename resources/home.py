from .base_resource import BaseResource
import os


class Home(BaseResource):

    def get(self):

        return {"message": "Hello, World!"}
