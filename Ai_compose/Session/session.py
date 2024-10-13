import reflex as rx
from Ai_compose.Backend.API.api_config import user


class Session(rx.State):
    authenticated: bool = False
    token: str = ""
    id: int = 0
    firstname: str = ""
    lastname: str = ""
    username: str = ""
    email: str = ""

    def procces_login(self, formdata:dict):
        username = formdata['username']
        password = formdata['password']
        user_data = user.login_user(
            username=username,
            password=password
        )

        try:
            self.token = user_data['token']
            self.id = user_data['user']['id']
            self.firstname = user_data['user']['firstname']
            self.lastname = user_data['user']['lastname']
            self.username = user_data['user']['username']
            self.email = user_data['user']['email']
            self.authenticated = True
            return True
        except:
            return False
        
    def sign_up(self):
        raise NotImplementedError("Implementar creación de cuenta")

    def logout(self):
        self.token = ""
        self.id = 0
        self.username = ""
        self.firstname = ""
        self.lastname = ""
        self.email = ""
        self.authenticated = False

    @rx.var
    def is_authenticated(self):
        if self.authenticated:
            return True
        return False
