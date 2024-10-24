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
                width='auto',
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
                rx.link(
                    rx.button('Cancelar'),
                    href='/'
                ),
                spacing="2",
                justify="center",
                margin_top='1rem'
            ),
            direction="column",
            margin_bottom="1.5rem",
            spacing="2",
        ),
        on_submit=AuthState.register,
        reset_on_submit=True,
        direction="column",
        maring_y="1rem",
        spacing="2",
    )


def signup_form():
    return (
        rx.card(
            form_header(),
            form_content(),
            padding="3",
            max_width="28em",
            size="4",
            width="100%",
        ),
    )


# def signup_form() -> rx.Component:
#     return rx.card(
#         rx.vstack(
#             rx.center(
#                 rx.image(
#                     src="/logo.jpg",
#                     width="2.5em",
#                     height="auto",
#                     border_radius="25%",
#                 ),
#                 rx.heading(
#                     "Create an account",
#                     size="6",
#                     as_="h2",
#                     text_align="center",
#                     width="100%",
#                 ),
#                 direction="column",
#                 spacing="5",
#                 width="100%",
#             ),
#             rx.vstack(
#                 rx.text(
#                     "Email address",
#                     size="3",
#                     weight="medium",
#                     text_align="left",
#                     width="100%",
#                 ),
#                 rx.input(
#                     rx.input.slot(rx.icon("user")),
#                     placeholder="user@reflex.dev",
#                     type="email",
#                     size="3",
#                     width="100%",
#                 ),
#                 justify="start",
#                 spacing="2",
#                 width="100%",
#             ),
#             rx.vstack(
#                 rx.text(
#                     "Password",
#                     size="3",
#                     weight="medium",
#                     text_align="left",
#                     width="100%",
#                 ),
#                 rx.input(
#                     rx.input.slot(rx.icon("lock")),
#                     placeholder="Enter your password",
#                     type="password",
#                     size="3",
#                     width="100%",
#                 ),
#                 justify="start",
#                 spacing="2",
#                 width="100%",
#             ),
#             rx.box(
#                 rx.checkbox(
#                     "Agree to Terms and Conditions",
#                     default_checked=True,
#                     spacing="2",
#                 ),
#                 width="100%",
#             ),
#             rx.button("Register", size="3", width="100%"),
#             rx.center(
#                 rx.text("Already registered?", size="3"),
#                 rx.link("Sign in", href="#", size="3"),
#                 opacity="0.8",
#                 spacing="2",
#                 direction="row",
#                 width="100%",
#             ),
#             spacing="6",
#             width="100%",
#         ),
#         max_width="28em",
#         size="4",
#         width="100%",
#     )
