import reflex as rx
from .state import ToneMakerState


def triggerbutton(icon_name: str, tooltip: str = ""):
    return rx.flex(
        rx.tooltip(
            rx.icon_button(
                icon_name,
                color_scheme="gray",
                variant="ghost",
                cursor="pointer",
                margin_x="0.2rem",
            ),
            content=tooltip,
        ),
        padding_y="0.5rem",
    )


def dropdown():
    options = {
        "maj": "mayor",
        "m": "menor",
        "maj7": "mayor septima",
        "m7": "menor septima",
    }
    return rx.menu.root(
        rx.menu.trigger(triggerbutton("chevron-down", tooltip="Seleccionar un tono")),
        rx.menu.content(
            rx.menu.item(
                options["maj"], on_click=ToneMakerState.set_tone(options["maj"])
            ),
            rx.menu.item("menor", on_click=ToneMakerState.set_tone(options["m"])),
            rx.menu.item(
                options["maj7"], on_click=ToneMakerState.set_tone(options["maj7"])
            ),
            rx.menu.item(
                options["m7"], on_click=ToneMakerState.set_tone(options["m7"])
            ),
        ),
    )
