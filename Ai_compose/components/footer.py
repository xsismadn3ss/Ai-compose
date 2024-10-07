import reflex as rx

def footer():
    return rx.center(
        rx.divider(color="pink", margin_bottom="2vh"),
        rx.text("© 2024 AiCompose. Todos los derechos reservados"),
        direction="column"
    )