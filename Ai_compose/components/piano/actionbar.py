import reflex as rx
from rxconfig import light_border, dark_border


def action_bar(*components: rx.Component):

    return rx.flex(
        rx.flex(components),
        border=rx.color_mode_cond(light=light_border, dark=dark_border),
        text_align="center",
        justify="center",
        border_radius="0.8rem",
        width="fit-content",
        margin_y="1rem",
        align="center",
    )
