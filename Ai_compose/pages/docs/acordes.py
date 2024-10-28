import reflex as rx
from ...templates.master import template
from ...components.markdown_render import markdown
from ...components.docs_menu.menu import doc_menu
from .views.container import doc_card


url = "/docs/acordes"


@rx.page(route=url, title="¿Qué es un acorde?")
@template
def acordes():
    return doc_card(
        blur_menu_item="¿Qué es un acorde?",
        markdown_route="docs/Teoría/Acordes/Acordes.md"
    )


@rx.page(route=url+"/adiciones", title="Acordes con adiciones")
@template
def acordes_adiciones():
    return doc_card(
        "Acordes con adiciones",
        "docs/Teoría/Acordes/Acordes con adiciones.md"
    )


@rx.page(route=url+"/basicos", title="Acordes básicos")
@template
def acordes_basicos():
    return doc_card(
        "Acordes básicos",
        "docs/Teoría/Acordes/Acordes normales.md"
    )
