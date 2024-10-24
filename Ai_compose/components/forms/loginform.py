import reflex as rx
from Ai_compose.state.auth_state import AuthState

def form_header():
    return rx.flex(
        rx.card(
            rx.flex(
                rx.icon("music-2"),
                rx.heading(" Ai Compose"),
                direction="row",
            ),
        ),
        rx.heading("Ingresa tus credenciales", as_="h3"),
        direction="column",
        align="center",
        spacing="2",
    )


def register_link():
    return rx.link(
        rx.text("¿Aún no tienes una cuenta? Resgistrate aquí", size="2"),
        margin_y="0.3rem",
        href="/sign_up",
    )


def form():
    return rx.form(
        rx.flex(
            rx.input(placeholder="Nombre de usuario", name="username", radius="large"),
            rx.input(
                placeholder="Contraseña",
                name="password",
                type="password",
                radius="large",
            ),
            register_link(),
            rx.flex(rx.button("Inicar sesión", type="submit"), justify="center"),
            direction="column",
            margin_top="1.3rem",
            spacing="2",
        ),
        on_submit=AuthState.login,
        reset_on_submit=True,
    )


def login_form():
    return rx.card(
        form_header(),
        form(),
        size='4'
    )
