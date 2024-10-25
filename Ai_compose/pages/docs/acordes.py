import reflex as rx
from ...templates.master import template
from ...components.markdown_render import markdown
from ...components.docs_menu.menu import doc_menu
from .views.container import container


url = "/docs/acordes"


@rx.page(route=url, title="¿Qué es un acorde?")
@template
def acordes():
    return rx.container(
        rx.card(
            rx.flex(doc_menu(blur="¿Qué es un acorde?"), justify="end"),
            markdown("docs/Teoría/Acordes/Acordes.md"),
            size="3",
        ),
        justify="center",
        direction="column",
    )


@rx.page(route=url+"/adiciones", title="Acordes con adiciones")
@template
def acordes_adiciones():
    return container(
        rx.card(
            rx.flex(doc_menu("Acordes con adiciones"), justify="end"),
            markdown("docs/Teoría/Acordes/Acordes con adiciones.md"),
            size="3",
        )
    )


@rx.page(route=url+"/basicos", title="Acordes básicos")
@template
def acordes_basicos():
    return container(
        rx.card(
            rx.flex(doc_menu("Acordes básicos"), justify="end"),
            markdown("docs/Teoría/Acordes/Acordes normales.md"),
            size="3",
        ),
    )
