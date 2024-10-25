import reflex as rx
from ...templates.master import template
from ...components.docs_menu.menu import doc_menu


@rx.page(route="/docs", title="Documentación")
@template
def introduction():

    with open("./docs/Música.md", encoding="utf-8") as readme:
        content = readme.read()

    return rx.container(
        rx.card(
            rx.flex(
                doc_menu(blur='Introducción'),
                justify="end",
                position="sticky",
                top="1rem",
            ),
            rx.markdown(content),
            size='3',
        ),
        justify="center",
        direction="column",
    )
