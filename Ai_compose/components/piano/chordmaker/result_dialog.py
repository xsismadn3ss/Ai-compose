import reflex as rx
from .state import ChordMakerState
from ..keys import key
from rxconfig import black_keys_style, white_keys_style


def render_note(note: rx.Var):
    return rx.button(
        note,
        bg=rx.cond(
            note.contains("#"),
            '#303030',
            '#d1d1d1'
        ),
        color=rx.cond(
            note.contains('#'),
            '#d1d1d1',
            '#303030'
        ),
        border_radius='0.5rem',
        margin_x = '0.2rem',
        padding_y= '0.6rem'
    )


def result_content(data: dict):
    return rx.vstack(
        rx.heading(data["name"], color_scheme="purple"),
        rx.flex(
            rx.text("Nomeclatura: ", weight='bold'),
            rx.text("{} {}".format(data["root"], data["symbol"]), margin_left='0.5rem'),
        ),
        rx.divider(),
        rx.heading("Notas", size='5'),
        rx.flex(rx.foreach(ChordMakerState.notes, render_note)),
    )


def error_content():
    return rx.vstack(
        rx.heading("Error", color_scheme="red"),
        rx.text("Asegurate de seleccionar una nota y un tipo de acorde para empezar"),
    )


def result_dialog():
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.icon_button(
                "send-horizontal",
                color_scheme="gray",
                variant="ghost",
                cursor="pointer",
                margin_x="0.2rem",
                margin_y="0.2rem",
                on_click=ChordMakerState.generate_chord(),
            )
        ),
        rx.alert_dialog.content(
            rx.cond(
                ChordMakerState.is_error & ~ChordMakerState.is_loaded,
                error_content(),
                rx.cond(
                    ChordMakerState.is_loaded & ~ChordMakerState.is_error,
                    result_content(ChordMakerState.data),
                    rx.spinner(),
                ),
            ),
            rx.alert_dialog.cancel(
                rx.flex(
                    rx.button(
                        "Cerrar",
                        variant="soft",
                        on_click=ChordMakerState.clear(),
                        margin_top="1rem",
                        color_scheme="gray",
                    ),
                    justify="end",
                ),
            ),
            max_width='35rem'
        ),
    )