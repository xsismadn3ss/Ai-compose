import reflex as rx
from ..templates.master import template
from ..components.pricing_card import basic_card, advanced_card, premium_card

@rx.page('/pricing_plans', title='Pricing Plans')
@template
def pricing_plans():
    return rx.vstack(
        rx.tablet_and_desktop(
            rx.text(
                "Opciones de paquetes", weight="bold", size="8", margin="5vh",
            ),
        ),
        rx.mobile_only(
            rx.text(
                "Opciones de paquetes", weight="bold",  size="8", margin="2vh", 
            ),          
        ),
        rx.flex(
            basic_card,
            advanced_card,
            premium_card,
            direction="row",
            wrap="wrap",
            width="100%",
            justify="center",
            spacing="5",
            margin_bottom="3em",
        ),
    )