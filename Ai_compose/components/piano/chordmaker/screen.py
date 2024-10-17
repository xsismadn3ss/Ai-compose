import reflex as rx
from .state import ChordMakerState

light_border = "1px solid #d3d3d3"
dark_border = "1px solid #414141"

def result():
    return rx.flex(
        rx.text(
            ChordMakerState.get_data,
            color=rx.color_mode_cond("#303030", "#bdbdbd"),
            margin_x="1rem",
        ),
        rx.text(
            ChordMakerState.symbol,
            color=rx.color_mode_cond("#303030", "#bdbdbd"),
            margin_right="1rem",
        ),
        bg=rx.color_mode_cond(
            light="#bdbdbd",
            dark='#303030'
        ),
        padding_y="0.5rem",
        border_top_left_radius="0.8rem",
        border_bottom_left_radius="0.8rem",
    )

none_func = lambda: None

def icon_button(icon_name:str, on_click, tooltip: str = ""):
    return rx.tooltip(
        rx.flex(
            rx.icon_button(
                icon_name,
                color_scheme="gray",
                variant="ghost",
                cursor="pointer",
                margin_x="0.5rem",
                on_click=on_click,
            ),
            border_left=rx.color_mode_cond(light=light_border, dark=dark_border),
            padding_y="0.5rem",
        ),
        content=tooltip
    )

def drop_button(icon_name:str, tooltip:str=""):
    return rx.tooltip(
        rx.icon_button(
            icon_name,
            color_scheme="gray",
            variant='ghost',
            cursor='pointer',
            margin_x='0.5rem',
            padding_y='0.5rem'
        ),
        content=tooltip
    )


def chord_selector():
    return rx.menu.root(
        rx.menu.trigger(
            drop_button('chevron-down', tooltip='Seleccionar tipo de acordes')
        ),
        rx.menu.content(
            rx.menu.item(
                rx.heading("Selecciona un tipo de acorde", size='2', weight='medium')
            )
        )
    )
    # TODO: agregar drop down para seleccionar tipo de acorde
    # TODO: obtener la lista de proporciones utilizando la api
    ...


def screen():
    light_border = "1px solid #d3d3d3"
    dark_border = "1px solid #414141"

    return rx.flex(
        rx.flex(
            result(),
            chord_selector(),
            icon_button(icon_name="delete", on_click=ChordMakerState.clear(), tooltip='Borrar todo'),
            icon_button(icon_name="send-horizontal", on_click=ChordMakerState.generate_chord(), tooltip='Generar acorde'),
        ),
        border=rx.color_mode_cond(light=light_border, dark=dark_border),
        text_align="center",
        justify="center",
        border_radius="0.8rem",
        width="fit-content",
        margin_y="1rem",
        align="center",
    )
