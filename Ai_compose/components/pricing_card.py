import reflex as rx
from ..state.eth_state import EthState


def pricingCard(title: str, description: str, price: str):
    return rx.card(
        rx.heading(title, align="center", color_scheme="purple"),
        rx.flex(
            rx.icon("check", color="green"),
            rx.text(description),
            spacing="1",
            margin_top="1rem",
        ),
        rx.flex(
            rx.heading(price),
            rx.heading("ETH", color_scheme="purple"),
            spacing="1",
            justify="center",
            margin_y="1.5rem",
        ),
        rx.form(
            rx.input(value=title, name="plan", style={"visibility": "hidden"}),
            rx.input(value=price, name="price", style={"visibility": "hidden"}),
            rx.flex(
                rx.button("COMPRAR PAQUETE"),
                justify="center",
                width="center",
                type="submit",
            ),
            on_submit=EthState.buy_tokens,
            reset_on_submit=False,
        ),
        size="4",
    )


def basic():
    return pricingCard(
        title="Basico",
        description="50 tokens para usar",
        price="0.0001",
    )


def advanced():
    return pricingCard(
        title="Avanzado", description="100 tokens para usar", price="0.0002"
    )


def premium():
    return pricingCard(
        title="Premium", description="200 tokens para usar", price="0.0003"
    )
