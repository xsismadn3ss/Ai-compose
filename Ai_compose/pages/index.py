import reflex as rx
import rxconfig

from ..templates.master import template
from ..components.cards import features_cards
from ..components.navbar.navbar_buttons import signup_button
from ..components.github_card import github_card


@rx.page(route="/", title="Home")
@template
def index():
    return rx.center(
        rx.container(
            rx.heading(
                "Aprende de música. Sin límites.",
                as_="h2",
                align="center",
                trim="normal",
                size="8",
                margin_top="15vh",
            ),
            rx.text(
                "Herramientas profesionales para aprender sobre teoría musical al alcance de todos.",
                align="center",
                size="5",
                margin_bottom="2vh",
            ),
        ),
        signup_button(),
        rx.text(
            "Funcionalidades y documentación",
            weight="bold",
            size="6",
            margin_top="5rem",
        ),
        features_cards(),
        rx.divider(),
        rx.text(
            "Créditos", weight="bold", size="6", margin_bottom="5vh", margin_top="5vh"
        ),
        rx.flex(
            github_card(username="Haluuuu", description='Backend developer'),
            github_card(username="xsismadn3ss", description='Fullstack developer'),
            github_card("Alexandra-Rivera", description='Frontend developer'),
            direction="row",
            justify="center",
            align="center",
            spacing="5",
            margin_bottom="5vh",
            wrap="wrap",
        ),
        ##########
        direction="column",
        justify="center",
    )
