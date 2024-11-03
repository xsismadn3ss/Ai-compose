import json
from ..api_client import Methods
from .base_model import BaseModel


class Pyament(BaseModel):
    def __init__(self, api, **routes):
        super().__init__(api, **routes)

    def buytoken(self, token: str, plan_name: str, tx_hash: str):
        route = self.tokens
        data = json.dumps({"plan": plan_name, "tx_hash": tx_hash})
        return self.api.request(method=Methods.POST, data=data, route=route, token=token)

    def spenttoken(self, token:str):
        route = self.spent_tokens
        return self.api.request(
            method=Methods.GET, route=route, token=token
        )

    def payment_history(self):
        route = self.payments
        return self.api.request(
            method=Methods.GET, route=route
        )