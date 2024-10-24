import reflex as rx
from ..templates.master import template
from ..components.forms.loginform import login_form

@rx.page('/login', title='Iniciar sesión')
@template
def login_page():
    return rx.center(
        login_form()
    )