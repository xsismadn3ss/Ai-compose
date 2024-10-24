import reflex as rx

from ..templates.master import template
from ..components.forms.signupform import signup_form
from ..components.cards import register_succesfully
from ..state.auth_state import AuthState

@rx.page(route="/sign_up", title="Registrarse")
@template
def signup()-> rx.Component:
    return rx.center(
        rx.cond(
            AuthState.is_logged_in,
            register_succesfully(),
            signup_form()
        ),
        direction="column",
        justify="center"
    )
