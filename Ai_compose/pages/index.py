import reflex as rx
from rxconfig import config

from ..components.navbar import navbar
from ..components.cards import card
from ..components.credits import credit 
from ..components.footer import footer 
from ..components.navbar import signup_button
from ..components.sign_up import signup_form

@rx.page(route="/", title="Home")
def index():
    return rx.container(
        navbar(),
        rx.center(
            rx.container(
                rx.heading("Aprende de música. Sin límites.", as_="h2", align="center", trim="normal", size="8", margin_top="20vh"),
                rx.text("Herramientas profesionales para aprender sobre teoría musical al alcance de todos.", align="center", size="5", margin_bottom="2vh"),
        ),    
            signup_button(),
            direction="column",
            margin_bottom="20vh",   
        ),
        rx.text("Funcionalidades y documentación", weight="bold", size="6"),
        card(),
        rx.divider(),
        rx.text("Créditos",weight="bold", size="6", margin_bottom="5vh", margin_top="5vh"),
        credit(),
        footer(),
        spacing="10"
    )