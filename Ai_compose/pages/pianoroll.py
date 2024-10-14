import reflex as rx

from ..state.auth import AuthState
from ..templates.master import template
from ..components.piano_component import piano_roll
from ..components.cards import not_logged_ind_card as message_card
    


@rx.page(route="/piano_roll", title="Piano roll test")
@template
def painoRoll(auth: AuthState):
    return rx.cond(
        auth.logged_in,
        rx.center(
            rx.container(
                rx.heading(
                    "Generador de Acordes y Tonalidades", as_="h3", margin_top="10vh"
                ),
                rx.center(piano_roll(), margin_bottom="10vh"),
                rx.heading("Generador de Escalas", as_="h3", margin_bottom="5vh"),
                rx.center(
                    piano_roll(),
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
