import reflex as rx
from rxconfig import glow_bg_light


def feature_card(text: str, *args, **kwargs):
    return rx.card(
        rx.flex(
            rx.text(text, weight="bold"),
            direction="column",
            align="center",
            justify="center",
            height="9rem",
            width="15rem",
        ),
        *args,
        rx.flex(style=glow_bg_light),
        text_align="center",
        size="3",
        **kwargs
    )


def features_cards():
    return rx.flex(
        feature_card(
            "Experimenta con Acordes",
            rx.flex(
                rx.icon("music", color="gray"),
                rx.icon("music-4", color="gray"),
                spacing="2",
            ),
        ),
        feature_card(
            "Descubre Escalas y Tonalidades",
            rx.flex(
                rx.icon("file-music", color="gray"),
                rx.icon("audio-waveform", color="gray"),
                spacing="2",
            ),
        ),
        feature_card(
            "Chatbot con IA incluido",
            rx.flex(
                rx.icon("bot", color="gray"),
                rx.icon("messages-square", color="gray"),
                spacing="2",
            ),
        ),
        feature_card(
            "Documentación de teoría músical gratis",
            rx.flex(
                rx.icon("circle-check", color="gray"),
                rx.icon("book-open-text", color="gray"),
                spacing="2",
            ),
        ),
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


def register_succesfully():
    return rx.card(
        rx.flex(style=glow_bg_light),
        rx.heading("Bienvenido a Ai Compose", size="5", margin_botton="0.8rem"),
        rx.text("Ya has iniciado sesión"),
        rx.button("Comienza a aprender", on_click=rx.redirect("/piano_roll")),
        margin_top="4rem",
        size="3",
    )
