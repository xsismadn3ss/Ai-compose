import reflex as rx
from .state import ScaleMakerState
from .result_dialog import result_dialog
from ..icon_button import icon_button
from ..actionbar import action_bar


def prop_screen():
    return rx.flex(
        rx.text(
            ScaleMakerState.note,
            color=rx.color_mode_cond("#303030", "#bdbdbd"),
            margin_x="1rem",
        ),
        bg=rx.color_mode_cond("#bdbdbd", "#303030"),
        padding_y="0.5rem",
        border_top_left_radius="0.8rem",
        border_bottom_left_radius="0.8rem",
    )


def bar():
    return action_bar(
        prop_screen(), icon_button(icon_name="delete", on_click=ScaleMakerState.clear()),
        result_dialog(),
    )
