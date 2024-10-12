import reflex as rx


def feature_card(text: str, **kwargs):
    return rx.card(
        rx.flex(
            rx.text(text, weight='bold'),
            direction="column",
            align="center",
            justify='center',
            height="10rem",
            width="15rem",
        ),
        text_align="center",
        **kwargs
    )


def features_cards():
    return rx.flex(
        feature_card("Experimenta con Acordes"),
        feature_card("Descubre Escalas y Tonalidad "),
        feature_card("Chatbot con IA incluido"),
        feature_card("Documentación de teoría músical gratis"),
        spacing="4",
        justify='center',
        margin_top='5rem',
        margin_bottom='5rem',
        wrap="wrap",
    )
