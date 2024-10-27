import reflex as rx
from ..keys import key
from ..piano_container import piano
from .action_bar import bar
from .state import ScaleMakerState


def black_keys() -> rx.Component:
    return rx.flex(
        key("c#", True, on_click=ScaleMakerState.set_note("c#")),
        key("d#", True, on_click=ScaleMakerState.set_note("d#")),
        rx.tablet_and_desktop(rx.spacer(margin_x="0.4em")),
        rx.mobile_only(rx.spacer(margin_x="0.2em")),
        key("f#", True, on_click=ScaleMakerState.set_note("f#")),
        key("g#", True, on_click=ScaleMakerState.set_note("g#")),
        key("a#", True, on_click=ScaleMakerState.set_note("a#")),
    )


def white_keys() -> rx.Component:
    return rx.flex(
        key("c", on_click=ScaleMakerState.set_note("c")),
        key("d", on_click=ScaleMakerState.set_note("d")),
        key("e", on_click=ScaleMakerState.set_note("e")),
        key("f", on_click=ScaleMakerState.set_note("f")),
        key("g", on_click=ScaleMakerState.set_note("g")),
        key("a", on_click=ScaleMakerState.set_note("a")),
        key("b", on_click=ScaleMakerState.set_note("b")),
    )

def scale_maker() -> rx.Component:
    return rx.flex(
        bar(),
        piano(black_keys(), white_keys()),
        margin_y='0.8rem',
        direction='column',
        justify='center',
        align='center'
    )
