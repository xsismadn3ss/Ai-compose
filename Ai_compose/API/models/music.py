from ..api_client import *
from .base_model import BaseModel
from urllib import parse


class Notes(BaseModel):
    def __init__(self, api, **routes):
        super().__init__(api, **routes)

    def get(self, id: int | None = None):
        route = self.notes + str(id) if id else self.notes
        return self.api.request(method=Methods.GET, route=route)


class Scales(BaseModel):
    def __init__(self, api, **routes):
        super().__init__(api, **routes)

    def get(self, id: int | None = None):
        route = self.scales + str(id) if id else self.scales
        return self.api.request(method=Methods.GET, route=route)


class Tones(BaseModel):
    def __init__(self, api, **routes):
        super().__init__(api, **routes)

    def get(self, id: int | None):
        route = self.tones + str(id) if id else self.tones
        return self.api.request(method=Methods.GET, route=route)


class Chords(BaseModel):
    def __init__(self, api, **routes):
        super().__init__(api, **routes)

    def get(self, id: int | None = None):
        route = self.chords + str(id) if id else self.chords
        return self.api.request(method=Methods.GET, route=route)

    def generate(self, note:str, symbol:str):
        route: str = self.generate_chord.format(parse.quote(note), symbol)
        return self.api.request(method=Methods.GET, route=route)
