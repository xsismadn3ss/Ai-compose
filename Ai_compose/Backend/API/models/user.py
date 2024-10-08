import json
from ..api_client import Methods
from .base_model import BaseModel


class User(BaseModel):
    def __init__(self, api, **routes):
        super().__init__(api, **routes)

    def login_user(self, username: str, password: str):
        route = self.login
        data = json.loads({"username": username, "password": password})
        return self.__api.request(method=Methods.POST, data=data, route=route)

    def register_user(self, username: str, email: str, password: str):
        route = self.register
        data = json.loads({"username": username, "email": email, "password": password})
        return self.__api.request(method=Methods.POST, data=data, route=route)

    def user_account(self, token: str, id: int):
        route = self.account
        return self.__api.request(method=Methods.GET, route=route, token=token)
