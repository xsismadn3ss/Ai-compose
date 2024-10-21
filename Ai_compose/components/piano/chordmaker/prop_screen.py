import reflex as rx
from .state import ChordMakerState

def prop_screen():
    return rx.flex(
        rx.text(
            ChordMakerState.get_data,
            color=rx.color_mode_cond("#303030", "#bdbdbd"),
            margin_x="1rem",
        ),
        rx.text(
            ChordMakerState.symbol,
            color=rx.color_mode_cond("#303030", "#bdbdbd"),
            margin_right="1rem",
        ),
        bg=rx.color_mode_cond(light="#bdbdbd", dark="#303030"),
        padding_y="0.5rem",
        border_top_left_radius="0.8rem",
        border_bottom_left_radius="0.8rem",
    )