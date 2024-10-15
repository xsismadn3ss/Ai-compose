import json
from ..api_client import Methods
from .base_model import BaseModel


class User(BaseModel):
    def __init__(self, api, **routes):
        super().__init__(api, **routes)

    def login_user(self, username: str, password: str):
        route = self.login
        data = json.dumps({"username": username, "password": password})
        return self.api.request(method=Methods.POST, data=data, route=route)

    def register_user(
        self,
        username: str,
        firstname: str,
        lastname: str,
        email:str,
        password:str
    ):
        route = self.register
        data = json.dumps(
            {
                "username": username,
                "email": email,
                "firstname": firstname,
                "lastname": lastname,
                "password": password,
            }
        )
        return self.api.request(method=Methods.POST, data=data, route=route)

    def user_account(self, token: str, id: int):
        route = self.account.format(id)
        return self.api.request(method=Methods.GET, route=route, token=token)
