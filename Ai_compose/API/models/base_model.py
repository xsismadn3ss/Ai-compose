from ..api_client import API


class BaseModel:
    def __init__(self, api: API, **routes: str):
        self.api = api
        for key, value in routes.items():
            setattr(self, key, value)
