import reflex as rx

from ..templates.master import template
from ..components.forms.signupform import signup_form

@rx.page(route="/sign_up", title="Registrarse")
@template
def signup()-> rx.Component:
    return rx.center(
        signup_form(),
        direction="column",
        justify="center"
    )
