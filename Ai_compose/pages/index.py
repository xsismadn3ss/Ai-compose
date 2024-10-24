import reflex as rx

from ..templates.master import template
from ..components.cards import features_cards
from ..components.buttons import signup_button, start_button
from ..components.github_card import github_card
from ..state.auth_state import AuthState


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
            ),
            rx.text(
                "Herramientas profesionales para aprender sobre teoría musical al alcance de todos.",
                align="center",
                size="5",
                margin_bottom="1rem",
            ),
            margin_top="4rem",
        ),
        rx.cond(AuthState.is_logged_in, start_button(), signup_button()),
        rx.spacer(margin_y="4rem"),
        rx.divider(),
        rx.tablet_and_desktop(
            rx.text(
                "Funcionalidades y documentación",
                weight="bold",
                size="6",
                margin_top="3rem",
            ),
        ),
        rx.mobile_only(
            rx.text(
                "Funcionalizades y documentación",
                size='4',
                weight='bold',
                margin_top='3rem'
            )
        ),
        features_cards(),
        rx.divider(),
        rx.text(
            "Créditos", weight="bold", size="6", margin_bottom="5vh", margin_top="5vh"
        ),
        rx.flex(
            github_card(username="Haluuuu", description="Backend developer"),
            github_card(username="xsismadn3ss", description="Fullstack developer"),
            github_card("Alexandra-Rivera", description="Frontend developer"),
            github_card("ingrid", description="Backend developer"),
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
