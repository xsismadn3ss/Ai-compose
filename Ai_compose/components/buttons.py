import reflex as rx
from .login_form import login_form_dialog


def signup_button():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Comienza a aprender", size="4", border_radius="0.6em", cursor="pointer"
            )
        ),
        login_form_dialog(),
    )


def start_button():
    return rx.link(
        rx.button(
            "Comienza a aprender", size="4", border_radius="0.6em", cursor="pointer"
        ),
        href="/piano_roll",
    )
