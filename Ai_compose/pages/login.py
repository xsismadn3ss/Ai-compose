import reflex as rx
from ..templates.master import template
from ..components.forms.loginform import login_form
from ..components.cards import register_succesfully as message_card
from ..state.auth_state import AuthState

@rx.page('/login', title='Iniciar sesión')
@template
def login_page():
    return rx.center(
        rx.cond(
            AuthState.is_logged_in,
            message_card(),
            login_form(),
        )
    )