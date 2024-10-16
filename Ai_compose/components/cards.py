import reflex as rx
from rxconfig import glow_bg_light


def feature_card(text: str, **kwargs):
    return rx.card(
        rx.flex(
            rx.text(text, weight="bold"),
            direction="column",
            align="center",
            justify="center",
            height="10rem",
            width="15rem",
        ),
        rx.flex(style=glow_bg_light),
        text_align="center",
        size="3",
        **kwargs
    )


def features_cards():
    return rx.flex(
        feature_card("Experimenta con Acordes"),
        feature_card("Descubre Escalas y Tonalidades"),
        feature_card("Chatbot con IA incluido"),
        feature_card("Documentación de teoría músical gratis"),
        spacing="4",
        justify="center",
        margin_top="3rem",
        margin_bottom="5rem",
        wrap="wrap",
    )


def not_logged_ind_card():
    return rx.card(
        rx.flex(style=glow_bg_light),
        rx.heading("Necesitas iniciar sesión", size="5", margin_bottom="0.8rem"),
        rx.text("Inicia sesión para acceder a este contenido", margin_bottom="0.8rem"),
        rx.button("Ir a inicio", on_click=rx.redirect("/")),
        margin_top="4rem",
        size="3",
    )
