import reflex as rx
from ..components.navbar.navbar import navbar
from Ai_compose.templates.master import chat_template
from .state import State
from ..state.auth_state import AuthState
from ..components.cards import not_logged_in_card


def qa(question: str, answer: str) -> rx.Component:
    return rx.flex(
        rx.divider(),
        rx.flex(
            rx.card(
                rx.text(question),
                border="1px solid purple",
                max_width="30rem",
                size="3",
            ),
            justify="end",
        ),
        rx.flex(
            rx.markdown(answer),
            margin_top="1.5rem",
            justify="start",
            direction="column",
        ),
        spacing="3",
        margin_top="2em",
        margin_bottom="4rem",
        direction="column",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(State.chat_history, lambda messages: qa(messages[0], messages[1]))
    )


def input_area(bg: str) -> rx.Component:
    return rx.text_area(
        value=State.question,
        placeholder="Has una pregunta",
        on_change=State.set_question,
        size="2",
        width="18rem",
        background=bg,
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.color_mode_cond(
                light=input_area(bg="#e3e3e3"), dark=input_area(bg="#202020")
            ),
            rx.flex(
                rx.icon_button("send-horizontal", on_click=State.answer),
                rx.icon_button("rotate-ccw", on_click=State.clear_history),
                direction="column",
                spacing="1",
            ),
            spacing="2",
            position="fixed",
            bottom="1.5rem",
        ),
        background="inherit",
        justify="center",
        width="100%",
    )


@rx.page(route="/chats", title="chats")
@chat_template
def chat() -> rx.Component:
    return rx.cond(
            AuthState.is_logged_in,
            rx.container(
            chat(), action_bar(),
            ),
            rx.center(
                not_logged_in_card()
            ),
        )
