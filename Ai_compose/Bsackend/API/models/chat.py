import json
from .base_model import BaseModel
from ..api_client import API, Methods


class Chat(BaseModel):
    def __init__(self, api: API, **routes: str):
        super().__init__(api, **routes)

    def get(self, token: str, id: int, messages: dict):
        route = self.chat.format(id)
        data = json.dumps({"messages": messages})
        return self.__api.request(method=Methods.GET, route=route, token=token)

    def create(self, token: str, messages: dict):
        route = self.new_chat
        data = json.loads({"messages": messages})
        return self.__api.request(method=Methods.POST, route=route, token=token)

    def patch(self, token: str, id: int, messages: dict):
        route = self.chat.format(id)
        data = json.dumps({"message": messages})
        return self.__api.request(method=Methods.PATCH, route=route, token=token)

    def delete(self, token, id):
        route = self.chat.format(id)
        return self.__api.request(method=Methods.DELETE, token=token)
