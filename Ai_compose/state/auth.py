import reflex as rx
from .base import State
from Ai_compose.API.api_config import user

class AuthState(State):
    token: str
    id: str
    username: str
    password: str
    confirm_password: str
    firstname: str
    lastname: str
    email: str

    def login(self):

        if self.username == "" or self.password == "":
            return rx.window_alert("Por favor ingresa correctamente tus datos")

        user_data = user.login_user(
            username=self.username,
            password=self.password
        )

        if 'token' in user_data:
            self.token = user_data['token']
            self.firstname = user_data['user']['firstname']
            self.lastname = user_data['user']['lastname']
            self.email = user_data['user']['email']
            self.authenticated = True

            return rx.toast.success("Bienvenido {}".format(self.username), position="top-center")

        else:
            self.authenticated = False
            return rx.toast.error('Usuario o contraseña no validos', position="top-center")