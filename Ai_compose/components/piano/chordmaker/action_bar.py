import reflex as rx
from rxconfig import light_border, dark_border
from .state import ChordMakerState
from .dropdown import dropdown
from .icon_button import icon_button
from .send_button import send_button
from .prop_screen import prop_screen

def action_bar():

    return rx.flex(
        rx.flex(
            prop_screen(),
            dropdown(),
            icon_button(icon_name="delete", on_click=ChordMakerState.clear()),
            send_button(),
        ),
        border=rx.color_mode_cond(light=light_border, dark=dark_border),
        text_align="center",
        justify="center",
        border_radius="0.8rem",
        width="fit-content",
        margin_y="1rem",
        align="center",
    )