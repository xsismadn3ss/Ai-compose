import reflex as rx


class MenuState(rx.ComponentState):
    selected: str = ""


def menu_item(title: str, route: str = "#"):
    return rx.menu.item(
        title,
        text_decoration=rx.cond(MenuState.selected == title, "underline", "none"),
        on_click=rx.redirect(route),
    )


def doc_menu(blur: str = ""):
    MenuState.selected = blur
    return rx.menu.root(
        rx.menu.trigger(rx.icon_button("book", variant="soft")),
        rx.menu.content(
            menu_item("Introducción", "/docs"),
            rx.menu.sub(
                rx.menu.sub_trigger("Acordes"),
                rx.menu.sub_content(
                    menu_item("¿Qué es un acorde?", "/docs/acordes"),
                    menu_item("Acordes básicos", "/docs/acordes/basicos"),
                    menu_item("Acordes de quinta", "/docs/acordes/potencia"),
                    menu_item("Acordes de séptima", "/docs/acordes/septima"),
                    menu_item("Acordes de sexta", "/docs/acordes/sexta"),
                    menu_item(
                        "Acordes con suspendidos", "/docs/acordes/suspendidos"
                    ),
                    menu_item("Acordes con adiciones", "/docs/acordes/adiciones"),
                ),
            ),
            menu_item("Escalas", '/docs/escalas'),
        ),
    )
