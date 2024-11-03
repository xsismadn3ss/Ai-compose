import reflex as rx

# from Ai_compose.components.forms.loginform import login_form
from Ai_compose.templates.master import chat_template


@rx.page(route="/chatbot", title="Crear plantilla de chatbot")
@chat_template
def test():
    return rx.container(
        rx.flex(
            rx.card(rx.text("Hello world"), border="1px solid gray"), justify="end"
        ),
        rx.flex(
            rx.card(rx.text("Hello user"), border="1px solid violet"), justify="start"
        ),
        rx.hstack(
        rx.hstack(
            rx.input(placeholder="Has una pregunta", size="2", width='20rem'),
            rx.icon_button("send-horizontal"),
            spacing="2",
            position="fixed",
            bottom="1rem",
        ),
            justify="center",
            width='100%'
        )
    )
