import reflex as rx


def navbar_logo():
    return rx.flex(
        rx.flex(rx.icon("music-2"), radius="full", padding="1rem"),
        rx.heading("Ai Compose", size="8"),
        spacing="2",
        align="center",
    )
