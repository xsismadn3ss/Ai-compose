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
    
@rx.page(route=url+"/septima", title="Acordes de séptima")
@template
def acordes_septima():
    return doc_card(
        "Acordes de séptima",
        "docs/Teoría/Acordes/Acordes de séptima.md"
    )
    
@rx.page(route=url+"/sexta", title="Acordes de sexta")
@template
def acordes_sexta():
    return doc_card(
        "Acordes de sexta",
        "docs/Teoría/Acordes/Acordes de sexta.md"
    )

@rx.page(route=url+"/suspendidos", title="Acordes de suspendidos")
@template
def acordes_suspendidos():
    return doc_card(
        "Acordes de suspendidos",
        "docs/Teoría/Acordes/Acordes suspendidos.md"
    )
    
@rx.page(route=url+"/potencia", title="Acordes de potencia")
@template
def acordes_potencia():
    return doc_card(
        "Acordes de potencia",
        "docs/Teoría/Acordes/Acordes de potencia.md"
    )   