import reflex as rx
from ..login_form import login_form_dialog
from ...Session.session import Session


def icon_button(icon_name: str):
    return rx.icon(icon_name)


def navbar_link(text: str, url: str):
    return rx.link(rx.text(text, size="3", weight="bold"), href=url)


def signup_button():
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Comienza a aprender", size='4', border_radius="0.6em", cursor='pointer')),
        login_form_dialog(),
    )

def logout_button():
    return rx.button(
        "Cerrar sesión",
        size = "2",
        border_radius = '0.6rem',
        on_click = Session.logout()
    )


def login_button():
    return rx.flex(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    "Iniciar sesión",
                    size="2",
                    border_radius = "0.6rem"
                )
            ),
            login_form_dialog(),
        )
    )
