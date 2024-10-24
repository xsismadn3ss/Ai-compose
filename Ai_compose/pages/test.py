import reflex as rx
from ..templates.master import template
from ..components.piano.chordmaker.chord_maker import chord_maker
from ..components.piano.tonemaker.tone_maker import tone_maker

# def login_card(auth):
#     return rx.vstack(
#         rx.text("Nombre de usuario"),
#         rx.input(placeholder="ingresa tu nombre de usuario", name='username', on_blur=auth.set_username),
#         rx.text("Contraseña"),
#         rx.input(placeholder="ingresa tu contraseña", name='password', type='password', on_blur=auth.set_password),
#         rx.button("Enviar", on_click=auth.login),
#     )


@rx.page(route="/test", title="Test")
@template
def test_page():
    return rx.center(
        # rx.container(
        #     login_card(auth),
        #     rx.divider(),
        #     rx.cond(
        #         auth.logged_in,
        #         rx.text("Sesión iniciada"),
        #         rx.text("Sesión cerrada"),
        #     )
        # ),
        rx.divider(),
        rx.container(
            rx.heading("Chord Maker", size='6', margin_y='1.5rem'),
            chord_maker(),
        ),
        rx.container(
            rx.heading("Tone Maker", size='6', margin_y='1.5rem'),
            tone_maker(),
        ),
        ##########
        direction="column",
        justify="center",
    )
