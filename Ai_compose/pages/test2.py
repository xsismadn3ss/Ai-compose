import reflex as rx
from Ai_compose.components.forms.loginform import login_form
from Ai_compose.templates.layout import template


@rx.page(route='/test2', title='Test using cookies')
@template
def test():
    return rx.center(
        login_form(),
        direction='column', 
        justify='center'
    )