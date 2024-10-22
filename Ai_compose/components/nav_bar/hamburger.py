import reflex as rx
from Ai_compose.state.auth_state import AuthState


class LoginState(rx.State):
    def login_toast(self) -> rx.Component:
        return rx.toast.warning("Implementar inicio de sesión")


def theme_button():
    return rx.menu.sub_content(
        rx.color_mode_cond(
            rx.menu.item(
                rx.flex(rx.icon("moon-star"), rx.text("Modo oscuro"), spacing="2"),
                on_click=rx.style.set_color_mode("dark"),
            ),
            rx.menu.item(
                rx.flex(rx.icon("sun"), rx.text("Modo claro"), spacing="2"),
                on_click=rx.style.set_color_mode("light"),
            ),
        ),
        rx.menu.item(
            rx.desktop_only(rx.icon("laptop")),
            rx.tablet_only(rx.icon("tablet")),
            rx.mobile_only(rx.icon("smartphone")),
            rx.text("Sistema"),
            on_click=rx.style.set_color_mode("system"),
        ),
    )

def login_logout_button():
    return rx.cond(
        AuthState.is_logged_id,
        rx.menu.item(
            'Cerrar sesión',
            color_scheme='red',
            on_click=AuthState.logout()
        ),
        rx.menu.item(
            'Inicir sesión',
            on_click=LoginState.login_toast()
        )
    )

def hamburguer():
    return rx.menu.root(
        rx.menu.trigger(rx.icon_button('menu', variant='ghost', margin_right='1rem')),
        rx.menu.content(
            rx.menu.item(
                'Inicio', on_click=rx.toast.warning("redireccionar a pagna de inicio que use cookies")
            ),
            rx.menu.item(
                'Piano Roll', on_click=rx.toast.warning("redireccionar a pagna de piano roll que use cookies")
            ),
            rx.menu.separator(),
            rx.menu.sub(
                rx.menu.sub_trigger(
                    'Tema'
                ),
                theme_button()
            ),
            rx.menu.separator(),
            login_logout_button()
        )
    )