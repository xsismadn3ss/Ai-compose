import reflex as rx
from rxconfig import glow_bg_light
from ..templates.master import template
from ..state.auth import AuthState

def login_card(auth):
    return rx.vstack(
        rx.text("Nombre de usuario"),
        rx.input(placeholder="ingresa tu nombre de usuario", name='username', on_blur=auth.set_username),
        rx.text("Contraseña"),
        rx.input(placeholder="ingresa tu contraseña", name='password', type='password', on_blur=auth.set_password),
        rx.button("Enviar", on_click=auth.login),
    )


@rx.page(route="/test", title="Test")
@template
def test_page(auth: AuthState):
    return rx.center(
        rx.container(
            login_card(auth),
            rx.divider(),
            rx.cond(
                auth.logged_in,
                rx.text("Sesión iniciada"),
                rx.text("Sesión cerrada"),
            )
        ),
        ##########
        direction="column",
        justify="center",
    )
