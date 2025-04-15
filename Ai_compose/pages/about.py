import reflex as rx
from ..templates.master import template
from rxconfig import bg_transparent_light, bg_transparent_dark
from ..components.piano.chordmaker.chord_maker import chord_maker


def info_card(*args):
    return rx.color_mode_cond(
        rx.card(
            args,
            size="3",
            max_width="40rem",
            margin_top="1.5rem",
            margin_bottom="2.5rem",
            style=bg_transparent_light,
        ),
        rx.card(
            args,
            size="3",
            max_width="40rem",
            margin_top="1.5rem",
            margin_bottom="1.5rem",
            style=bg_transparent_dark,
        ),
    )


def m1():
    return rx.flex(
        rx.heading("Reflexion"),
        rx.markdown(
            r"""
            ```python
            class Routes:
                def __init__(self, **routes):
                    for key, value in routes.items():
                        setattr(self, key, value)
            ```
            """,
            font_size="15px",
        ),
        align='center',
        justify='center',
        direction='column'
    )


def m2():
    return rx.container(
        rx.heading("Inyección de dependencias"),
        rx.markdown(
            r"""
                ```python
                routes = Routes(
                    tones="/tones/",
                    scales="/scales/",
                    chords="/chords/",
                    notes="/notes/",
                    login="/login/",
                    register="/register/",
                    account="/account/",
                    chat="/chat/{}",
                    new_chat="/chat/create/",
                    payments="/payments/",
                    tokens="/buy_tokens/",
                    spent_tokens="/ask/",
                )
                ```
                """,
            font_size="15px",
        ),
    )


@rx.page(route="/about", title="Saber más")
@template
def about():
    return rx.center(
        rx.heading("¿Qué es Ai Compose?"),
        info_card(
            rx.text(
                "Nuestro sitio web permite aprender de forma autodidacta a aquellos usuarios que estan interesados en la música y les interesa crear algo nuevo y fresco por su cuenta. Por el momento nuestro sitio aborda temás basicos y fundamentales de composición como aprender que es una escala, un acordes y una tonalidad, ademas de mostrar como se compone y como se puede utilizar para crear musica nueva."
            ),
            # rx.container(chord_maker()),
        ),
        rx.heading("Framework Utilizado"),
        info_card(
            rx.flex(rx.logo(), justify="center"),
            rx.text(
                rx.text.strong("REFLEX"),
                " es un framework fullstack de Python relativamente nuevo, su versión oficial fue lanzada en 2023. Utilizando Reflexion permite crear interfaces web sin escribir HTML y refleja todo en componentes de React usando NEXT JS. ",
                rx.text.strong("REFLEX "),
                "permite inyectar CSS, para personalizar perzonalizar los compoentes y darles un poco más de estética",
            ),
            rx.markdown(
                r"""
                ### Ejemplo
                ```python
                black_keys_style = {
                    "bg": "#303030",
                    "border_radius": "0.5em",
                    "margin_x": "0.4em",
                    "margin_bottom": "0.4em",
                }

                white_keys_style = {
                    "bg": "#f4eaff",
                    "border_radius": "0.5em",
                    "margin_x": "0.2em",
                    "color": "#202020",
                    "height": "4.2rem"
                }
                ```
                """,
                font_size="15px",
            ),
            rx.markdown(
                r"""
                ```python
                import reflex as rx
                from rxconfig import black_keys_style, white_keys_style


                def key(note: str, is_black: bool = False, on_click=None) -> rx.Component:
                    if is_black:
                        style = black_keys_style

                    else:
                        style = white_keys_style

                    return (
                        rx.tablet_and_desktop(
                            rx.button(note.upper(), style=style, on_click=on_click, size="3"),
                        ),
                        rx.mobile_only(
                            rx.button(note.upper(), style=style, on_click=on_click, size="2")
                        ),
                    )
                ```
                """,
                font_size="15px",
            ),
        ),
        rx.heading("Técnicas de programación utilizadas"),
        rx.desktop_only(
            rx.flex(
                info_card(m1()),
                info_card(m2()),
                spacing="4",
            ),
        ),
        rx.mobile_and_tablet(
            rx.flex(info_card(m1()), info_card(m2()), direction="column")
        ),
        direction="column",
        justify="center",
        margin_x="1rem",
    )
