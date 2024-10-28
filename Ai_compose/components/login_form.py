import reflex as rx
from Ai_compose.state.auth_state import AuthState
from .dark_light_dialog_content import dark_light_dialog as dialog_content

def form_header():
    return (
        rx.flex(
            rx.card(
                rx.flex(
                    rx.icon("music-2"),
                    rx.heading(" Ai Compose"),
                    direction="row",
                ),
                background=rx.color_mode_cond(
                    'rgba(183, 159, 255, 0.8)',
                    'inherit',
                )
            ),
            rx.heading("Ingresa tus credenciales", as_="h4"),
            direction="column",
            align="center",
            spacing="2",
        ),
    )


def form_fields():
    return rx.flex(
        rx.text("Nombre de usuario", weight="bold"),
        rx.input(
            placeholder="ingresa tu nombre de usuario", on_blur=AuthState.set_username
        ),
        rx.spacer(margin_y="1rem"),
        rx.text("Contraseña", weight="bold"),
        rx.input(
            placeholder="ingresa tu contraseña",
            type="password",
            on_blur=AuthState.set_password,
        ),
        direction="column",
        margin_top="1.3rem",
    )


def form_link():
    return rx.link(
        rx.text("¿Aún no tienes una cuenta? Haz click aquí", margin_y="0.8em"),
        href="/sign_up",
    )


def login_form_button():
    return rx.button("Ingresar", on_click=AuthState.login_from_dialog())


def login_form_dialog():
    return dialog_content(
        form_header(),
        form_fields(),
        form_link(),
        rx.flex(
            rx.dialog.close(
                login_form_button(),
            ),
            rx.dialog.close(rx.button("Cancelar")),
            spacing="4",
            justify="center",
        ),
    )
