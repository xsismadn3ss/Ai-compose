import reflex as rx
from rxconfig import light_border, dark_border


def icon_button(icon_name: str, on_click) -> rx.Component:
    return rx.flex(
            rx.icon_button(
                icon_name,
                color_scheme="gray",
                variant="ghost",
                cursor="pointer",
                margin_x="0.5rem",
                on_click=on_click,
            ),
        border_left=rx.color_mode_cond(light=light_border, dark=dark_border),
        padding_y="0.5rem",
    )
