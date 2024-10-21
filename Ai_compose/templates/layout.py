from typing import Callable
import reflex as rx

from ..components.footer import footer


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.heading("Navbar here"),
            padding="0",
            width="100%",
            style={
                "position": "fixed",
                "top": "0",
                "background": "transparent",
                "backdrop_filter": "blur(20px)",
            },
            z_index="1000",
        ),
        rx.flex(
            page(),
            style={"margin_top": "5rem", "padding": "0.5rem"},
            direction="column",
            width="100%",
        ),
        rx.flex(margin_bottom="8rem"),
        footer(),
        width="100%",
        direction="column",
    )
