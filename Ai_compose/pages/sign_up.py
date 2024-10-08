import reflex as rx
from ..components.navbar import navbar
from ..components.sign_up import signup_form

@rx.page(route="/sign_up", title="Sign Up Form")
def signup()-> rx.Component:
    return rx.center(
        navbar(),
        signup_form(),
        direction="column"
    )
