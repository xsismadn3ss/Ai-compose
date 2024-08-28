import reflex as rx


@rx.page(route="/piano_roll", title="Piano roll test")
def painoRoll():
    return rx.center(
        rx.color_mode.button(position="top-right"),
        rx.flex(
            rx.flex(
                rx.card("C#", margin_left="1.2em", bg_color="#7a7a7a"),
                rx.card("D#", margin_right="3em", bg_color="#7a7a7a"),
                rx.card("F#", bg_color="#7a7a7a"),
                rx.card("G#", bg_color="#7a7a7a"),
                rx.card("A#", bg_color="#7a7a7a"),
                spacing="3",
            ),
            rx.flex(
                rx.card("C", padding="1.2em", bg_color="black"),
                rx.card("D", padding="1.2em", bg_color="black"),
                rx.card("E", padding="1.2em", bg_color="black"),
                rx.card("F", padding="1.2em", bg_color="black"),
                rx.card("G", padding="1.2em", bg_color="black"),
                rx.card("A", padding="1.2em", bg_color="black"),
                rx.card("B", padding="1.2em", bg_color="black"),
                spacing="1",
                margin_top="0.4em",
            ),
            direction="column",
            border_radius="1em",
            border="1px solid grey",
            padding="0.8em",
            bg="linear-gradient(80deg, #3a353e, #5a3737, #402b50, #762242, #3a353e)",
            margin_top="10em",
            box_shadow="0px 0px 50px 3px #924337",
        ),
    )
