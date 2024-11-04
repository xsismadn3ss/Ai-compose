import reflex as rx
from ..templates.master import template
from ..state.profile_state import ProfileState
from ..state.auth_state import AuthState
from ..components.walletform import wallet_dialog
from ..components.cards import not_logged_in_card as message_card


def username():
    return rx.heading(ProfileState.username, color_scheme="purple")


def coins():
    return rx.flex(
        rx.icon("coins", color="green"),
        rx.text("{} Tokens".format(ProfileState.left_coins), weight="bold", size="3"),
        spacing="2",
    )


def wallet_info():
    return rx.flex(
        rx.text.strong("Cartera: "),
        rx.text(ProfileState.wallet_addres),
        spacing="2",
    )


def balance_info():
    balance = ProfileState.balance
    return rx.flex(
        rx.text.strong("Saldo:"),
        rx.text("{} ETH".format(balance), color_scheme="gray"),
        spacing="2",
    )


def profile_card():
    return rx.flex(
        rx.heading("Perfil", align="center", margin_bottom="2rem", size="6"),
        rx.card(
            username(),
            coins(),
            rx.cond(
                ProfileState.valid_pk & ProfileState.pk != "",
                rx.container(
                    wallet_info(),
                    balance_info(),
                ),
            ),
            rx.flex(
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button("Conectar tarjeta"),
                    ),
                    wallet_dialog(),
                ),
                rx.button(
                    "Desconectar tarjeta", on_click=ProfileState.disconnect_wallet
                ),
                margin_top="1.2rem",
                spacing="3",
            ),
        ),
        direction="column",
    )


@rx.page(
    "/account",
    title="Ai compose - {}".format(ProfileState.username) if AuthState.is_logged_in else "Mi perfil",
    description="Ai compose. Aprende de teoría músical de forma autodidacta",
)
@template
def profile():
    return rx.center(
        rx.cond(
            AuthState.is_logged_in,
            profile_card(),
            message_card(),
        ),
        direction="column",
        spacing="2",
    )
