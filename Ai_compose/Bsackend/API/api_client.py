import json
import requests


class Methods:
    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"


class Routes:
    def __init__(self, **routes):
        for key, value in routes.items():
            setattr(self, key, value)


class API:
    def __init__(self, server_url: str, headers: dict):
        self.url = server_url
        self.__headers__ = headers

    def __as_json(self, response: requests.Response):
        return json.loads(response.text)

    def request(
        self, method: str, data: dict | None = None, route: str = "", token: str = ""
    ):
        auth = self.__headers__
        auth["Authorization"] = token
        response = requests.request(
            method=method, url=self.url + route, data=data, headers=auth
        )
        return self.__as_json(response)
