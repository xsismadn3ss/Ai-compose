import reflex as rx
from .prop_screen import prop_screen
from .dropdown import dropdown
from ..actionbar import action_bar
from ..icon_button import icon_button
from .result_dialog import result_dialog
from .state import ToneMakerState


def bar():
    return action_bar(
        prop_screen(),
        dropdown(),
        icon_button(icon_name='delete', on_click=ToneMakerState.clear()),
        result_dialog(),
    )
