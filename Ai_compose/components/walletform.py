import reflex as rx
from .dark_light_dialog_content import dark_light_dialog as dialog_content
from ..state.profile_state import ProfileState


def form_header():
    return rx.flex(
        rx.card(
            rx.flex(
                rx.icon("music-2"),
                rx.heading(" Ai Compose"),
                direction="row",
            ),
        ),
        rx.heading("Conectar cartera de Metamask", as_="h3"),
        direction="column",
        align="center",
        spacing="2",
    )


def form_fields():
    return rx.flex(
        rx.text("Clave privada", weight="bold"),
        rx.input(
            placeholder="ingresa tu clave privada",
            on_blur=ProfileState.set_input_pk,
            type="password",
        ),
        direction="column",
        margin_top="1.5rem",
        margin_bottom="2rem",
    )


def confirm_button():
    return rx.button("Conectar", on_click=ProfileState.connect_wallet())


def wallet_dialog():
    return dialog_content(
        form_header(),
        form_fields(),
        rx.flex(
            rx.dialog.close(confirm_button()),
            rx.dialog.close(rx.button("Cancelar")),
            spacing="4",
            justify="center",
        ),
    )
