import reflex as rx
from ....components.markdown_render import markdown
from ....components.docs_menu.menu import doc_menu

def doc_card(blur_menu_item:str, markdown_route:str):
    """
    ## Doc card
    Crea un tarjeta para renderizar archivos markdown y mostrar en la seccion de documentación

    Args
    * blur_menu_item: especifica que titulo deseas sombrear en el menu, asegurate que ese item exista en el indice y se llame exactamente igual.
    * markdown: especifica la ruta relativa del archivo markdown a renderizar.

    ### Nota
    Puedes agregar nuevos items en el indice ``components/docs_menu/menu.py``

    """
    return rx.container(
        rx.card(
            rx.flex(
                doc_menu(
                    blur=blur_menu_item
                ),
                justify="end",
                width='100%'
            ),
            markdown(
                markdown_route
            ),
            size="2"
        ),
        justify='center',
        direction='column'
    )
