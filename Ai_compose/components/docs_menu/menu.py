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
                    menu_item("¿Qué es un acorde?"),
                    menu_item("Acordes básicos"),
                    menu_item("Acordes de quinta"),
                    menu_item("Acordes de séptima"),
                    menu_item("Acordes de sexta"),
                    menu_item("Acordes con suspendidos"),
                    menu_item("Acordes con adiciones"),
                ),
            ),
            menu_item("Escalas"),
        ),
    )
