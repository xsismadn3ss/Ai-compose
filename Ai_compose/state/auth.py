import reflex as rx
from .base import State
from .fx.validations import validate_email, validate_password
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

        user_data = user.login_user(username=self.username, password=self.password)

        if "token" in user_data:
            self.token = user_data["token"]
            self.firstname = user_data["user"]["firstname"]
            self.lastname = user_data["user"]["lastname"]
            self.email = user_data["user"]["email"]
            self.authenticated = True

            return rx.toast.success(
                "Bienvenido {}".format(self.username), position="top-center"
            )

        else:
            self.authenticated = False
            return rx.toast.error(
                "Usuario o contraseña no validos", position="top-center"
            )

    def register(self):
        print(self.__dict__)
        if (
            self.username == ""
            or self.password == ""
            or self.confirm_password == ""
            or self.firstname == ""
            or self.lastname == ""
            or self.email == ""
        ):
            return rx.window_alert("Los datos ingresados son invalidos")

        elif self.password != self.confirm_password:
            return rx.window_alert("Las contraseñas no coinciden")

        else:
            email_valid=validate_email(self.email)
            password_valid=validate_password(self.password)

            if not email_valid: return rx.window_alert("El email no es valido")
            if not password_valid: return rx.window_alert("La contraseña no es valida")
            
            else:
                print("Usuario guardado con exito ✅")
                return rx.toast.success("Usuario creado con exito", position="top-center")

