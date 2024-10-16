import reflex as rx

from Ai_compose.state.auth import AuthState
from ..templates.master import template
from ..components.cards import features_cards
from ..components.navbar.navbar_buttons import signup_button
from ..components.github_card import github_card


@rx.page(route="/", title="Home")
@template
def index(auth:AuthState):
    return rx.center(
        rx.container(
            rx.heading(
                "Aprende de música. Sin límites.",
                as_="h2",
                align="center",
                trim="normal",
                size="8",
            ),
            rx.text(
                "Herramientas profesionales para aprender sobre teoría musical al alcance de todos.",
                align="center",
                size="5",
                margin_bottom="1rem",
            ),
            margin_top="4rem"
        ),
        signup_button(auth),
        rx.spacer(margin_y='4rem'),
        rx.divider(),
        rx.text(
            "Funcionalidades y documentación",
            weight="bold",
            size="6",
            margin_top="3rem",
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
