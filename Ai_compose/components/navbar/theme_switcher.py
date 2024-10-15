import reflex as rx

def theme_switch():
    return rx.flex(
        rx.popover.root(
            rx.popover.trigger(
                rx.button(
                    rx.icon("sun-moon"),
                    variant="soft",
                    color_scheme="gray",
                    border_radius="0.6rem",
                )
            ),
            rx.popover.content(
                rx.vstack(
                    rx.color_mode_cond(
                        rx.button(
                            rx.icon("moon"),
                            rx.text("Tema oscuro"),
                            variant="ghost",
                            on_click=rx.style.set_color_mode("dark"),
                            outline="none",
                        ),
                        rx.button(
                            rx.icon("sun"),
                            rx.text("Tema claro"),
                            variant="ghost",
                            on_click=rx.style.set_color_mode("light"),
                            outline="none",
                        ),
                    ),
                    rx.button(
                        rx.icon("laptop"),
                        rx.text("Sistema"),
                        variant="ghost",
                        on_click=rx.style.set_color_mode("system"),
                        outline="none",
                    ),
                )
            ),
        )
    )
