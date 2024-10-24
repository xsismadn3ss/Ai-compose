import reflex as rx
from ..state.auth import AuthState


def form_header():
    return rx.flex(
        rx.card(
            rx.flex(
                rx.icon("music-2"),
                rx.heading("Ai Compose"),
                direction="row",
            ),
        ),
        rx.heading("Crea una cuenta", as_="h4"),
        direction="column",
        align="center",
        spacing="2",
    )


def form_fields():
    return rx.flex(
        rx.text("Username", weight="bold"),
        rx.input(placeholder="Ingresa tu username", type="text", on_blur=AuthState.set_username),
        rx.text("Email", weight="bold"),
        rx.input(placeholder="correo@ejemplo.com", type="email", on_blur=AuthState.set_email),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.flex(
                    rx.text("Nombres", weight="bold", text_align="left"),
                    rx.input(placeholder="Ingresa tus nombres", type="text", on_blur=AuthState.set_firstname),
                    spacing="2",
                    direction="column",
                    width="100%",
                ),
                rx.flex(
                    rx.text("Apellidos", weight="bold"),
                    rx.input(placeholder="Ingresa tus apellidos", type="text", on_blur=AuthState.set_lastname),
                    spacing="2",
                    direction="column",
                    width="100%",
                ),
                spacing="2",
                direction="column",
            ),
        ),
        rx.desktop_only(
            rx.flex(
                rx.flex(
                    rx.text("Nombres", weight="bold", text_align="left"),
                    rx.input(placeholder="Ingresa tus nombres", type="text", on_blur=AuthState.set_firstname),
                    spacing="2",
                    direction="column",
                    width="100%",
                ),
                rx.flex(
                    rx.text("Apellidos", weight="bold"),
                    rx.input(placeholder="Ingresa tus apellidos", type="text", on_blur=AuthState.set_lastname),
                    spacing="2",
                    direction="column",
                    width="100%",
                ),
                justify="between",
                spacing="2",
            ),
        ),
        rx.text("Password", weight="bold"),
        rx.input(placeholder="Ingresa tu contraseña", type="password", on_blur=AuthState.set_password),
        rx.text("Confirmar contraseña", weight="bold"),
        rx.input(placeholder="Confirma tu contraseña", type="password", on_blur=AuthState.set_confirm_password),
        direction="column",
        margin_y="3vh",
        spacing="5",
    )


def register_button():
    return (rx.button("Registrarse", size="3", width="100%"))


def signup_form(auth:AuthState) -> rx.Component:

    return rx.container(
        rx.desktop_only(
            rx.card(
                form_header(),
                form_fields(),
                register_button(),  
                padding="3em",
                width="40rem",
                margin_top="0.3em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.card(
                form_header(),
                form_fields(),
                register_button(),    
                padding="3em",
                max_width="40rem",
                margin_top="1vh",
            ),
        ),
    )
