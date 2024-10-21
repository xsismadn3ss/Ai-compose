import reflex as rx

from ..templates.master import template
from ..components.navbar.navbar import navbar
from ..components.sign_up import signup_form

@rx.page(route="/sign_up", title="Sign Up Form")
@template
def signup(auth)-> rx.Component:
    return rx.center(
        signup_form(auth),
        direction="column",
        justify="center"
    )
