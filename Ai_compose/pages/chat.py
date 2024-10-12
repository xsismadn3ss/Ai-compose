import reflex as rx
from ..components.navbar.navbar import navbar

@rx.page(route="/chats", title="chats")
def chat()->rx.Component:
    return rx.container(
        navbar(),
        rx.heading("Chats", margin_top="5vh")
    )