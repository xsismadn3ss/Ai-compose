import reflex as rx
from ....API.api_config import chords
from .state import ChordMakerState


def get_options() -> list:
    response = chords.get()
    proportions: list = []

    for item in response:
        proportions.append([item["c_type"], item["symbol"]])

    return proportions


def drop_button(icon_name: str, tooltip: str = ""):
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


def render_item(item):
    type = item[0]
    symbol = item[1]
    return rx.menu.item(
        f"{type} ({symbol})", on_click=ChordMakerState.set_symbol(symbol)
    )


def dropdown():
    options = get_options()
    return rx.menu.root(
        rx.menu.trigger(
            drop_button("chevron-down", tooltip="Seleccionar tipo de acordes")
        ),
        rx.menu.content(
            rx.menu.item(
                "Obtener acordes",
            ),
            rx.menu.separator(),
            rx.foreach(options, render_item),
        ),
    )
