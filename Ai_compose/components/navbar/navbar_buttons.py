import reflex as rx
from ..login_form import login_form_dialog
from Ai_compose.state.auth import AuthState


def icon_button(icon_name: str):
    return rx.icon(icon_name)


def navbar_link(text: str, url: str):
    return rx.link(rx.text(text, size="3", weight="bold"), href=url)


def signup_button(auth:AuthState):
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Comienza a aprender", size='4', border_radius="0.6em", cursor='pointer')),
        login_form_dialog(auth),
    )

def logout_button():
    return rx.button(
        "Cerrar sesión",
        size = "2",
        border_radius = '0.6rem',
        on_click = AuthState.logout
    )


def login_button(auth:AuthState):
    return rx.flex(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    "Iniciar sesión",
                    size="2",
                    border_radius = "0.6rem"
                )
            ),
            login_form_dialog(auth),
        )
    )
