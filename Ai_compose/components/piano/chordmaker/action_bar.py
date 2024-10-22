from .state import ChordMakerState
from .dropdown import dropdown
from ..icon_button import icon_button
from .result_dialog import result_dialog
from ..actionbar import action_bar
from .prop_screen import prop_screen


def bar():
    return action_bar(
        prop_screen(),
        dropdown(),
        icon_button(icon_name="delete", on_click=ChordMakerState.clear()),
        result_dialog(),
    )
