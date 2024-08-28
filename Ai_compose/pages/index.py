import reflex as rx
from rxconfig import config


@rx.page(route="/", title="Home")
def index():
    return rx.text("Home")