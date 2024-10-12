import reflex as rx
from ..login_form import login_form


def icon_button(icon_name: str):
    return rx.icon(icon_name)


def navbar_link(text: str, url: str):
    return rx.link(rx.text(text, size="3", weight="bold"), href=url)


def signup_button():
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Comienza a aprender", size='4', border_radius="0.6em", cursor='pointer')),
        login_form(),
    )


def login_button():
    return rx.flex(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.icon_button(
                    rx.icon("user"),
                    size="2",
                    radius="full",
                )
            ),
            login_form(),
        )
    )
