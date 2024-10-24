import reflex as rx
from ..API.api_config import user
from .fx.validations import validate_email, validate_password


class AuthState(rx.State):
    token: str = rx.LocalStorage("")
    form_data: dict = {}
    username: str = ""
    password: str = ""

    def logout(self):
        self.token = ""

    def login(self, form_data: dict) -> rx.Component:
        if form_data["username"] == "" or form_data["password"] == "":
            return rx.toast.error(
                "Campos vacios, asegurate de ingresar bien tus datos",
                position="top-center",
            )

        user_data = user.login_user(
            username=form_data["username"], password=form_data["password"]
        )

        if "token" in user_data:
            self.token = user_data["token"]

            return rx.toast.success(
                "Bienvenido {}".format(form_data["username"]), position="top-center"
            )

        else:
            return rx.toast.error(
                "Usuario o contraseña no validos, asegurate de ingresar correctamente tus datos",
                position="top-center",
            )

    def login_from_dialog(self) -> rx.Component:
        if self.username == "" or self.password == "":
            return rx.toast.error(
                "Campos vacios, asegurate de ingresar bien tus datos",
                position="top-center",
            )

        user_data = user.login_user(username=self.username, password=self.password)
        self.username = ""
        self.password = ""

        if "token" in user_data:
            self.token = user_data["token"]

            return rx.toast.success(
                "Bienvenido {}".format(self.username), position="top-center"
            )

        else:
            return rx.toast.error(
                "Usuario o contraseña no validos, asegurate de ingresar correctamente tus datos",
                position="top-center",
            )

    def register(self, form_data: dict) -> rx.Component:
# {'username': 'abraham', 'firstname': 'klklkl', 'lastname': 'correo@example.con', 'password': '2477klk', 'confirm_password': 'klklklk'}
        if (
            form_data["username"] == ""
            or form_data["firstname"] == ""
            or form_data["lastname"] == ""
            or form_data["email"] == ""
            or form_data["password"] == ""
            or form_data["confirm_password"] == ""
        ):
            return rx.toast.warning(
                "Asegurate de rellenar todos los campos", position="top-center"
            )

        elif form_data["password"] != form_data["confirm_password"]:
            return rx.toast.error("Las contraseñas no coinciden", position="top-center")

        else:
            valid_email = validate_email(form_data["email"])
            valid_password = validate_password(form_data["password"])

            if not valid_email:
                return rx.toast.warning(
                    "El correo electrónico no es válido", position="top-center"
                )
            if not valid_password:
                return rx.toast.error(
                    "La contraseña no es valida", position="top-center"
                )

            else:
                user_data = user.register_user(
                    username=form_data["username"],
                    firstname=form_data["firstname"],
                    lastname=form_data["lastname"],
                    email=form_data["email"],
                    password=form_data["password"]
                )
                self.token = user_data['token']
                print("Usuario guardado con exito ✅")
                return rx.toast.success(
                    "Usuario creado con exito", position="top-center"
                )

    @rx.var
    def is_logged_in(self):
        return self.token != ""
