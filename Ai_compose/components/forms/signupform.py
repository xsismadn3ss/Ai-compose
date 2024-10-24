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
        rx.heading("Ingresa tu datos", as_="h4"),
        direction="column",
        align="center",
        spacing="2",
    )


def label(title):
    return rx.text(title, weight="bold", margin_top="0.6rem", color_scheme="gray")


def field(placeholder: str, type: str, name: str, icon_name: str):
    return rx.input(
        rx.input.slot(rx.icon(icon_name)),
        placeholder=placeholder,
        type=type,
        name=name,
        radius="large",
        width="100%",
    )


def form_content():
    return rx.form(
        rx.flex(
            label("Nombre de usuario"),
            field(
                placeholder="crea un nombre de usuario",
                type="text",
                name="username",
                icon_name="at-sign",
            ),
            rx.flex(
                rx.vstack(
                    label("Nombre"),
                    field(
                        placeholder="ingresa tus nombre",
                        type="text",
                        name="firstname",
                        icon_name="whole-word",
                    ),
                ),
                rx.vstack(
                    label("Apellido"),
                    field(
                        placeholder="ingresa tus apellidos",
                        type="text",
                        name="lastname",
                        icon_name="whole-word",
                    ),
                ),
                spacing="2",
                max_width="26rem",
                width="auto",
            ),
            label("Correo electrónico"),
            field(
                placeholder="correo@example.com",
                type="email",
                name="email",
                icon_name="mail",
            ),
            label("Contraseña"),
            field(
                placeholder="crea un contraseña",
                type="password",
                name="password",
                icon_name="key",
            ),
            label("Confirmar contraseña"),
            field(
                placeholder="confirma tu contraseña",
                type="password",
                name="confirm_password",
                icon_name="circle-check-big",
            ),
            rx.flex(
                rx.button("Registrarse", type="submit"),
                rx.link(rx.button("Cancelar"), href="/"),
                spacing="2",
                justify="center",
                margin_top="1rem",
            ),
            direction="column",
            margin_bottom="1.5rem",
            spacing="2",
        ),
        on_submit=AuthState.register,
        reset_on_submit=False,
        direction="column",
        maring_y="1rem",
        spacing="2",
    )


def signup_form():
    return rx.card(
        form_header(),
        form_content(),
        padding="3",
        max_width="28em",
        size="4",
        width="100%",
    )
