import reflex as rx
# from rxconfig import card_style

glow_bg_light = {
    'box_shadow': '0px 0px 4.5rem 1rem #9563ee',
}


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
        rx.flex(style=glow_bg_light),
        text_align="center",
        size='3',
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
        margin_top='3rem',
        margin_bottom='5rem',
        wrap="wrap",
    )
