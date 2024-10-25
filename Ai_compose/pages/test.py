import reflex as rx
from ..templates.master import template
from ..components.piano.chordmaker.chord_maker import chord_maker
from ..components.piano.tonemaker.tone_maker import tone_maker


@rx.page(route="/test", title="Test")
@template
def test_page():
    return rx.center(
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
