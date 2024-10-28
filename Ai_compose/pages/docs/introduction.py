import reflex as rx
from ...templates.master import template
from ...components.docs_menu.menu import doc_menu
from ...components.markdown_render import markdown


@rx.page(route="/docs", title="Documentación")
@template
def introduction():
    return rx.container(
        rx.card(
            rx.flex(
                doc_menu(blur="Introducción"),
                justify="end",
            ),
            markdown("./docs/Música.md"),
            size="3",
        ),
        justify="center",
        direction="column",
    )
