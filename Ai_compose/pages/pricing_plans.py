import reflex as rx
from ..templates.master import template
from ..components.pricing_card import basic, advanced, premium


@rx.page(
    "/pricing",
    title="Comprar tokens",
    description="Compra nuestros tokens para usar en nuestra aplicación 👍",
)
@template
def pricing_plans():
    return rx.center(
        rx.container(
            rx.flex(
                rx.icon("coins", color="green", size=40),
                rx.heading("Comprar tokens", align='left', size="8"),
                spacing="3",
            ),
        ),
        rx.text(
            "Elije el paquete que más se adecue a tus necesidades. Los tokens comprados en nuestra página se pueden utilizar para realizar preguntas a nuestra IA.",
            style={
                "text_align": "justify",
                "margin_bottom": "2rem",
                "max_width": "40rem",
            },
        ),
        rx.flex(
            basic(),
            advanced(),
            premium(),
            direction="row",
            wrap="wrap",
            width="100%",
            justify="center",
            spacing="5",
            margin_bottom="3em",
        ),
        direction="column",
        justify="center",
    )
