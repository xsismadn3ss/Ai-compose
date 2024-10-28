import reflex as rx
from ...templates.master import template
from ...components.markdown_render import markdown
from ...components.docs_menu.menu import doc_menu
from .views.container import doc_card


url = "docs/Teoría"

@rx.page(route=url+"/melodia", title="¿Qué es una Melodía?")
@template
def melodia():
    return doc_card(
        blur_menu_item="¿Qué es una Melodia?",
        markdown_route="docs/Teoría/Melodía.md"
    )
    
@rx.page(route=url+"/metrica", title="¿Qué es una Métrica?")
@template
def metrica():
    return doc_card(
        blur_menu_item="¿Qué es una Métrica?",
        markdown_route="docs/Teoría/Métrica.md"
    )
    
@rx.page(route=url+"/notas", title="¿Qué es una Nota?")
@template
def nota():
    return doc_card(
        blur_menu_item="¿Qué es una Nota?",
        markdown_route="docs/Teoría/Notas.md"
    )
    
@rx.page(route=url+"/progresion_acordes", title="¿Qué es una Progresión de acordes?")
@template
def progresion_acordes():
    return doc_card(
        blur_menu_item="¿Qué es una Progresión de acordes?",
        markdown_route="docs/Teoría/Progresión de acordes.md"
    )
    
@rx.page(route=url+"/tonalidad", title="¿Qué es una Tonalidad?")
@template
def tonalidad():
    return doc_card(
        blur_menu_item="¿Qué es una Tonalidad?",
        markdown_route="docs/Teoría/Tonalidad.md"
    )