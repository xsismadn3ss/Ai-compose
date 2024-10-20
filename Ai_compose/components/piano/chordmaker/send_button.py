import reflex as rx
from .state import ChordMakerState
from .icon_button import icon_button


def send_button():
    return icon_button(
        icon_name="send-horizontal",
        on_click=ChordMakerState.generate_chord()
    )