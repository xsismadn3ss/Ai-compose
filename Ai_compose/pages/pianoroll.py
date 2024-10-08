import reflex as rx
from ..components.navbar import navbar
from ..components.footer import footer
from ..components.piano_component import piano_roll

@rx.page(route="/piano_roll", title="Piano roll test")
def painoRoll():
    return rx.container(
        navbar(),
        rx.heading("Generador de Acordes y Tonalidades", as_="h3", margin_top="10vh"),
        rx.center(
            piano_roll(),
            margin_bottom="10vh"
        ),
        rx.heading("Generador de Escalas", as_="h3", margin_bottom="5vh"),
        rx.center(
            piano_roll(),
            margin_bottom="10vh",
        ),
            footer(),
    )