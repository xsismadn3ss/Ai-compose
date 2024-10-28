import reflex as rx


def loading() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Generando tu respuesta...",
            color_scheme="gray",
            size="5",
        ),
        rx.spinner(),
        direction="column",
    )
