import reflex as rx
from ..components.navbar.navbar import navbar
from Ai_compose.templates.master import template

@rx.page(route="/chats", title="chats")
@template
def chat(auth)->rx.Component:
    return rx.container(
        rx.heading("Chats", margin_top="5vh")
    )