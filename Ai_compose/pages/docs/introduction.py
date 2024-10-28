import reflex as rx
from ...templates.master import template
from .views.container import doc_card


@rx.page(route="/docs", title="Documentación")
@template
def introduction():
    return doc_card(
        blur_menu_item="Introducción",
        markdown_route="./docs/Música.md"
    )
