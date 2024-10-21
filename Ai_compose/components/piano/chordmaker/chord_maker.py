import reflex as rx
from .state import ChordMakerState
from ..keys import key
from .action_bar import action_bar
from ..piano_container import piano


def black_keys() -> rx.Component:
    return rx.flex(
        key("c#", True, ChordMakerState.set_note("c#")),
        key("d#", True, ChordMakerState.set_note("d#")),
        rx.spacer(margin_x="0.4em"),
        key("f#", True, ChordMakerState.set_note("f#")),
        key("g#", True, ChordMakerState.set_note("g#")),
        key("a#", True, ChordMakerState.set_note("a#")),
    )


def white_keys() -> rx.Component:
    return rx.flex(
        key("c", on_click=ChordMakerState.set_note("c")),
        key("d", on_click=ChordMakerState.set_note("d")),
        key("e", on_click=ChordMakerState.set_note("e")),
        key("f", on_click=ChordMakerState.set_note("f")),
        key("g", on_click=ChordMakerState.set_note("g")),
        key("a", on_click=ChordMakerState.set_note("a")),
        key("b", on_click=ChordMakerState.set_note("b")),
    )


def chord_maker():
    return rx.flex(
        action_bar(),
        piano(
            black_keys(),
            white_keys(),
        ),
        margin_y="0.8em",
        direction="column",
        justify="center",
        align="center",
    )
