
import reflex as rx


class LoginState(rx.State):
    def login_toast(self) -> rx.Component:
        return rx.toast.warning("Implementar inicio de sesión")
    
    def logout_toast(self) -> rx.Component:
        return rx.toast.warning("Implementar inicion de sesión")

def hamburger():
    return rx.menu.root(
        rx.menu.trigger(rx.icon_button("menu", variant="ghost", margin_right="1rem")),
        rx.menu.content(
            rx.menu.item("Inicio", on_click=rx.redirect("/")),
            rx.menu.item("Piano Roll", on_click=rx.redirect("/piano_roll")),
            rx.menu.separator(),
            rx.menu.sub(
                rx.menu.sub_trigger("Tema"),
                rx.menu.sub_content(
                    rx.color_mode_cond(
                        rx.menu.item(
                            rx.flex(
                                rx.icon("moon-star"),
                                rx.text("Modo oscuro"),
                                spacing="2",
                            ),
                            on_click=rx.style.set_color_mode("dark"),
                        ),
                        rx.menu.item(
                            rx.flex(rx.icon("sun"), rx.text("Modo claro"), spacing="2"),
                            on_click=rx.style.set_color_mode("light"),
                        ),
                    ),
                    rx.menu.item(
                        rx.flex(rx.icon("laptop"), rx.text("Sistema"), spacing="2"),
                        on_click=rx.style.set_color_mode("system"),
                    ),
                ),
            ),
            rx.menu.separator(),
            rx.menu.item(
                'Iniciar sesión', on_click=LoginState.login_toast()
            ),
            rx.menu.item(
                rx.text("Cerrar sesión", color_scheme="red"), on_click=LoginState.login_toast()
            )
        ),
    )
