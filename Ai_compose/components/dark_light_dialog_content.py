import reflex as rx
from rxconfig import bg_transparent_light, bg_transparent_dark, bg_transparent_light2


def dark_light_dialog(*args):
    return rx.color_mode_cond(
        rx.dialog.content(
            args, padding="2em", max_width="26em", style=bg_transparent_light
        ),
        rx.dialog.content(
            args, padding="2em", max_width="26em", style=bg_transparent_dark
        ),
    )

def dark_light_alertdialog(*args):
    return rx.color_mode_cond(
        rx.alert_dialog.content(
            args, padding="2em", max_width="35rem", style=bg_transparent_light2
        ),
        rx.alert_dialog.content(
            args, padding="2em", max_width="35rem", style=bg_transparent_dark
        ),
    )
