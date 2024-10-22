import reflex as rx
from .state import ToneMakerState

def result_content(data:str|None=None):
    return rx.vstack(
        rx.heading("Tonalidad de {} {}".format(ToneMakerState.note, ToneMakerState.tone)),
        rx.markdown(data)
    )

def error_content():
    return rx.vstack(
        rx.heading('Error', color_scheme='red'),
        rx.text("Asegurate de seleccionar una nota y un tono para empezar")
    )

def result_dialog():
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.icon_button(
                'send-horizontal',
                color_scheme='gray',
                variant='ghost',
                cursor='pointer',
                margin_x='0.2rem',
                margin_y='0.2rem',
                on_click=ToneMakerState.generate_tone()
            )
        ),
        rx.alert_dialog.content(
            rx.cond(
                ToneMakerState.is_error & ~ToneMakerState.is_loaded,
                error_content(),
                rx.cond(
                    ToneMakerState.is_loaded & ~ToneMakerState.is_error,
                    result_content(),
                    rx.spinner()
                )
            ),
            rx.alert_dialog.cancel(
                rx.flex(
                    rx.button(
                        'Cerrar',
                        variant='soft',
                        on_click=ToneMakerState.clear(),
                        margin_top='1rem',
                        color_scheme='gray'
                    ),
                    justify='end'
                )
            )
        )
    )