import reflex as rx

from ..state.auth_state import AuthState
from ..templates.master import template
from ..components.piano_component import piano_roll
from ..components.cards import not_logged_in_card as message_card
from ..components.piano.chordmaker.chord_maker import chord_maker
from ..components.piano.tonemaker.tone_maker import tone_maker
from ..components.piano.scalemaker.scale_maker import scale_maker

@rx.page(route="/piano_roll", title="Piano roll", description='Explora acordes, tonalidades y escalas usando IA')
@template
def painoRoll():
    return rx.cond(
        AuthState.is_logged_in,
        rx.center(
            rx.container(
                rx.heading("Acordes y Tonalidades", as_="h3", margin_top="10vh"),
                rx.center(
                    rx.tabs.root(
                        rx.tabs.list(
                            rx.tabs.trigger("Generar acordes", value="tab1"),
                            rx.tabs.trigger("Generar tonalidades", value="tab2"),
                        ),
                        rx.tabs.content(
                            chord_maker(),
                            value="tab1",
                        ),
                        rx.tabs.content(
                            tone_maker(),
                            value="tab2",
                        ),
                        default_value="tab1",
                    ),
                    margin_bottom="10vh",
                ),
                rx.heading("Generador de Escalas", as_="h3", margin_bottom="5vh"),
                rx.center(
                    scale_maker(),
                    margin_bottom="10vh",
                ),
            ),
            direction="column",
            justify="center",
        ),
        rx.center(
            rx.vstack(
                message_card(),
                align="center",
                justify="center",
            )
        ),
    )
