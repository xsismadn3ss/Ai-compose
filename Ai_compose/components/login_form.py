import reflex as rx
from Ai_compose.Session.session import Session


class LoginForm_State(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data:dict):
        self.form_data = form_data
        is_authenticated = Session.procces_login(self.form_data)
        
        if is_authenticated:
            return rx.toast.success('Inicio de sesión exitoso')

        return rx.toast.error('Usuario o contraseña incorrrectos')

def login_form():
    return rx.form.root(
        rx.form.field(
            rx.flex(
                rx.form.label("Nombre de usuario"),
                rx.form.control(
                    rx.input(
                        placeholder="ingresa tu nombre de usuario",
                        type="text",
                    ),
                    as_child=True,
                ),
                direction="column",
                spacing="1",
                align="stretch",
            ),
            name="username",
        ),
        rx.form.field(
            rx.flex(
                rx.form.label("Contraseña"),
                rx.form.control(
                    rx.input(placeholder="ingresa tu contraseña", type="password"),
                    as_child=True,
                ),
                direction="column",
                spacing="1",
                align="stretch",
            ),
            name='password'
        ),
        rx.flex(
            rx.link(
                "¿No tienes una cuenta? Registrate aquí",
                href="/sign_up",
                size="2",
                color_scheme="purple",
            ),
        ),
        rx.flex(
            rx.form.submit(
                rx.button("Ingresar"),
                as_child=True,
            ),
            spacing='2',
            justify='center',
            margin_top="1rem"
        ),
        on_submit=lambda form_data: LoginForm_State.handle_submit(form_data),
        reset_on_submit=True,
    )


def login_form_dialog():
    return rx.dialog.content(
        rx.flex(
            rx.card(
                rx.flex(
                    rx.icon("music-2"),
                    rx.heading(" Ai Compose"),
                    direction="row",
                ),
            ),
            rx.heading("Ingresa tus credenciales", as_="h4"),
            direction="column",
            align="center",
            spacing="2",
        ),
        login_form(),
        padding="2em",
        max_width="28em",
    )
