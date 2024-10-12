import reflex as rx
from .logo import navbar_logo
from .hamburger import hamburger
from .theme_switcher import theme_switch
from .navbar_buttons import navbar_link, login_button


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.flex(
                navbar_logo(),
                rx.flex(
                    navbar_link("Inicio", "/"),
                    navbar_link("Piano Roll", "/piano_roll"),
                    rx.link(
                        rx.button(
                            rx.text("Chat", color_scheme="purple", weight="bold"),
                            rx.icon("messages-square"),
                            variant="soft",
                            color_scheme="gray",
                            border_radius="0.6em",
                        ),
                        href="/chats",
                    ),
                    rx.tooltip(theme_switch(), content="Cambiar tema"),
                    rx.tooltip(login_button(), content="Iniciar sesión"),
                    align="center",
                    margin_x="1rem",
                    spacing="4",
                ),
                justify="between",
                direction="row",
            ),
            rx.divider(),
            width="100%",
        ),
        rx.mobile_and_tablet(
            rx.flex(
                navbar_logo(),
                hamburger(),
                justify="between",
                direction="row",
                align="center",
            ),
            rx.divider(),
            width="100%",
        ),
    )
