import reflex as rx
from .state import ScaleMakerState
from ..loading_content import loading


def result_content(data: str | None = None):
    return rx.vstack(
        rx.heading("Escalas para la nota {}".format(ScaleMakerState.note)),
        rx.markdown(data),
    )


def error_content():
    return rx.vstack(
        rx.heading("Error", color_scheme="red"),
        rx.text("Asegurate de seleccionar una nota para generar el resultado"),
    )


def result_dialog():
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.icon_button(
                "send-horizontal",
                color_scheme="gray",
                variant="soft",
                cursor="pointer",
                margin_x="0.2rem",
                margin_y="0.2rem",
                on_click=ScaleMakerState.generate_scale(),
            )
        ),
        rx.alert_dialog.content(
            rx.cond(
                ScaleMakerState.is_error & ~ScaleMakerState.is_loaded,
                error_content(),
                rx.cond(
                    ScaleMakerState.is_loaded & ~ScaleMakerState.is_error,
                    result_content(data=ScaleMakerState.data),
                    loading(),
                ),
            ),
            rx.alert_dialog.cancel(
                rx.flex(
                    rx.button(
                        "Cerrar",
                        variant="soft",
                        on_click=ScaleMakerState.clear(),
                        margin_top="1rem",
                        color_scheme="gray",
                    ),
                    justify="end",
                )
            ),
        ),
    )
