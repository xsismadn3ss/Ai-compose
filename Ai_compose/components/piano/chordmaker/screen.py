import reflex as rx
from .state import ChordMakerState

def result():
    return rx.flex(
        rx.text(
            ChordMakerState.get_data,
            color=rx.color_mode_cond("white", "white"),
            margin_x="1rem",
        ),
        rx.text(
            ChordMakerState.symbol,
            color=rx.color_mode_cond("white", "white"),
            margin_right="1rem",
        ),
        bg="black",
        padding_y="0.5rem",
        border_top_left_radius="0.8rem",
        border_bottom_left_radius="0.8rem",
    )

none_func = lambda: None

def screen_button(icon_name:str, on_click = none_func(), tooltip: str = ""):
    light_border = "1px solid #d3d3d3"
    dark_border = "1px solid #414141"
    return rx.flex(
        rx.icon_button(
            icon_name,
            color_scheme="gray",
            variant="ghost",
            cursor="pointer",
            margin_x="0.5rem",
            on_click=on_click
        ),
        border_left=rx.color_mode_cond(light=light_border, dark=dark_border),
        padding_y="0.5rem",
    )

def chord_selector():
    # TODO: agregar drop down para seleccionar tipo de acorde
    # TODO: obtener la lista de proporciones utilizando la api
    ...


def screen():
    light_border = "1px solid #d3d3d3"
    dark_border = "1px solid #414141"

    return rx.flex(
        rx.flex(
            result(),
            screen_button("chevron-down"),
            screen_button("delete", on_click=ChordMakerState.clear()),
            screen_button("send-horizontal", on_click=ChordMakerState.generate_chord()),
        ),
        border=rx.color_mode_cond(light=light_border, dark=dark_border),
        text_align="center",
        justify="center",
        border_radius="0.8rem",
        width="fit-content",
        margin_y="1rem",
        align="center",
    )