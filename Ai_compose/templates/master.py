from typing import Callable
import reflex as rx

from ..components.footer import footer
from ..components.navbar.navbar import navbar
from ..state.auth import AuthState


def template(page: Callable[[], rx.Component], is_required:bool=False) -> rx.Component:
    if is_required:
        return  rx.redirect('/')



    return rx.flex(
        rx.flex(
            navbar(AuthState),
            padding="0",
            width="100%",
            direction="column",
            style={
                "position": "fixed",
                "top": "0",
                "background": 'transparent',
                'backdrop_filter': 'blur(20px)'
            },
            z_index='1000'
        ),
        rx.flex(
            page(AuthState),
            style={"margin_top": "5rem", 'padding': '0.5rem'},
            direction="column",
            width='100%'
        ),
        rx.flex(margin_bottom="8rem"),
        footer(),
        width="100%",
        direction='column'
    )
