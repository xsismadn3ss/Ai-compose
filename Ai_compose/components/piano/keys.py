import reflex as rx
from rxconfig import black_keys_style, white_keys_style


def key(note: str, is_black: bool = False, on_click=None) -> rx.Component:
    if is_black:
        style = black_keys_style

    else:
        style = white_keys_style

    return (
        rx.tablet_and_desktop(
            rx.button(note.upper(), style=style, on_click=on_click, size="3"),
        ),
        rx.mobile_only(
            rx.button(note.upper(), style=style, on_click=on_click, size="2")
        ),
    )
