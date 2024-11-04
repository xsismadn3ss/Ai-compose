import reflex as rx
from .base_eth import BaseEth
from ..API.api_config import user

class ProfileState(BaseEth):
    email:str = ''
    firstname:str = ''
    lastname:str = ''

    def request_data(self):
        if self.is_logged_in:
            data = user.user_account(
                self.token
            )
            return data
        return None
        
    @rx.var
    def username(self):
        data = self.request_data()
        if data: return data['username']
        return None
    
    @rx.var
    def user_email(self):
        data = self.request_data()
        if data:return data['email']
        return None
        
    @rx.var
    def firstname_user(self):
        data = self.request_data()
        if data: return data['firstname']
        return None
    
    @rx.var
    def lastname_user(self):
        data = self.request_data()
        if data: return data['lastname']
        return None

    @rx.var
    def left_coins(self):
        data = self.request_data()
        if data: return data['coins']
        return None