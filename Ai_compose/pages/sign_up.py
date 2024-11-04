import reflex as rx

from ..templates.master import template
from ..components.forms.signupform import signup_form
from ..components.cards import register_succesfully
from ..state.auth_state import AuthState


@rx.page(
    route="/sign_up",
    title="Ai Compose - Registrarse",
    description="Crea una nueva cuenta y aprende de teoría musical de forma autodidacta",
)
@template
def signup() -> rx.Component:
    return rx.center(
        rx.cond(AuthState.is_logged_in, register_succesfully(), signup_form()),
        direction="column",
        justify="center",
    )
