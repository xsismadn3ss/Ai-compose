import reflex as rx
from ..keys import key
from ..piano_container import piano
from .action_bar import bar
from .state import ToneMakerState


def black_keys() -> rx.Component:
    return rx.flex(
        key("c#", True, on_click=ToneMakerState.set_note('C#')),
        key("d#", True, on_click=ToneMakerState.set_note('D#')),
        rx.tablet_and_desktop(rx.spacer(margin_x="0.4em")),
        rx.mobile_only(rx.spacer(margin_x="0.2em")),
        key("f#", True, on_click=ToneMakerState.set_note('F#')),
        key("g#", True, on_click=ToneMakerState.set_note('G#')),
        key("a#", True, on_click=ToneMakerState.set_note('A#')),
    )


def white_keys() -> rx.Component:
    return rx.flex(
        key("c", on_click=ToneMakerState.set_note('C')),
        key("d", on_click=ToneMakerState.set_note('D')),
        key("e", on_click=ToneMakerState.set_note('E')),
        key("f", on_click=ToneMakerState.set_note('F')),
        key("g", on_click=ToneMakerState.set_note('G')),
        key("a", on_click=ToneMakerState.set_note('A')),
        key("b", on_click=ToneMakerState.set_note('B')),
    )


def tone_maker():
    return rx.flex(
        bar(),
        piano(black_keys(), white_keys()),
        margin_y="0.8rem",
        direction="column",
        justify="center",
        align="center",
    )
