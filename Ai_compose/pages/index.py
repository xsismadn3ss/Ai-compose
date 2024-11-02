import reflex as rx

from ..templates.master import template
from ..components.cards import features_cards
from ..components.buttons import signup_button, start_button
from ..components.github_card import github_card
from ..state.auth_state import AuthState


@rx.page(
    route="/", title="Inicio", description="Ai Compose aprende tería musical con IA"
)
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
                "Funcionalidades y documentación",
                size="4",
                weight="bold",
                margin_top="3rem",
            )
        ),
        features_cards(),
        rx.divider(),
        rx.text(
            "Creditos", weight="bold", size="6", margin_bottom="5vh", margin_top="5vh"
        ),
        rx.flex(
            github_card(username="Haluuuu", description="Backend developer"),
            github_card(username="xsismadn3ss", description="Fullstack developer"),
            github_card("Alexandra-Rivera", description="Frontend developer"),
            # github_card("ingrid", description="Backend developer"),
            direction="row",
            justify="center",
            align="center",
            spacing="5",
            margin_bottom="5vh",
            wrap="wrap",
        ),
        rx.divider(),
        rx.text(
            "Tenologías utilizadas",
            size="6",
            weight="bold",
            margin_top="4rem",
            margin_bottom="2rem",
        ),
        rx.card(
            rx.logo(),
            rx.flex(
                rx.image(src="/linux.svg", width="4rem"),
                rx.image(src="/django.svg", width="4rem"),
                rx.image(src="/github.svg", width="4rem"),
                rx.image(src="/postgresql.svg", width="4rem"),
                rx.image(src="/ethereum.svg", width="4rem"),
                rx.image(src="/markdown.svg", width="4rem"),
                spacing="5",
                justify="center",
                wrap="wrap",
            ),
            size="3",
            margin_bottom="2rem",
        ),
        rx.text(
            "Conocimientos adquiridos",
            size="6",
            weight="bold",
            margin_top="2rem",
            margin_bottom="1rem",
        ),
        rx.card(
            rx.flex(
                rx.blockquote("Django Rest Framework"),
                rx.blockquote("REFLEX"),
                rx.blockquote("Anti Prop Drilling"),
                rx.blockquote("Web3.py"),
                rx.blockquote("Railway"),
                rx.blockquote("INFURA"),
                rx.blockquote("LocalStorage"),
                rx.blockquote("Token Authentication"),
                rx.blockquote("Reflection"),
                rx.blockquote("Dependency Inyection"),
                spacing="2",
                wrap="wrap",
                justify="center",
            ),
            size='3',
            margin_bottom="3rem",
        ),
        ##########
        direction="column",
        justify="center",
    )
