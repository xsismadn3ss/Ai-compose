import reflex as rx
from .state import ToneMakerState

def prop_screen():
    return rx.flex(
        rx.text(
            ToneMakerState.note,
            color=rx.color_mode_cond('#303030', '#bdbdbd'),
            margin_x='1rem'
        ),
        rx.text(
            ToneMakerState.tone,
            color=rx.color_mode_cond('#303030', '#bdbdbd'),
            margin_right='1rem'
        ),
        bg=rx.color_mode_cond('#bdbdbd', '#303030'),
        padding_y='0.5rem',
        border_top_left_radius="0.8rem",
        border_bottom_left_radius="0.8rem",
    )