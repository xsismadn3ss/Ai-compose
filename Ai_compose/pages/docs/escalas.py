import reflex as rx
from ...templates.master import template
from ...components.markdown_render import markdown
from ...components.docs_menu.menu import doc_menu
from .views.container import doc_card


url = "/docs/escalas"

@rx.page(route=url, title="¿Qué es una escala?")
@template
def escalas():
    return doc_card(
        blur_menu_item="¿Qué es una escala?",
        markdown_route="docs/Teoría/Escalas/Escalas.md"
    )