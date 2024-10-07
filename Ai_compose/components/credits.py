import reflex as rx

def credit(): 
    return rx.grid(
        rx.center( 
            rx.avatar(src="https://avatars.githubusercontent.com/u/132961024?v=4", radius="full", width="10rem", height="10rem"),
            rx.text("Harold Herrera"),
            rx.center(
                rx.link("@Github: Haluuuu", href="https://github.com/Haluuuu", color_scheme="purple", target="blank"),
            ),
            spacing="4",
            direction="column"
        ),
        rx.center(
            rx.avatar(src="https://avatars.githubusercontent.com/u/132122513?v=4", radius="full", width="10rem", height="10rem"),
            rx.text("Abraham Artiga"),
            rx.center(
                rx.link("@Github: xsismadn3ss", href="https://github.com/xsismadn3ss", color_scheme="purple", target="blank"),
            ),
            spacing="4",
            direction="column"
        ),
        rx.center(
            rx.avatar(src="https://avatars.githubusercontent.com/u/91226679?v=4", radius="full", width="10rem", height="10rem"), 
            rx.text("Alexandra Rivera"),
            rx.center(
                rx.link("@Github: Alexandra-Rivera", href="https://github.com/Alexandra-Rivera", color_scheme="purple", target="blank"),
            ),
            spacing="4",
            direction="column"
        ),
        
        spacing="9",
        columns="3",
        width="100%",
        justify="center",
        margin_bottom="10vh"
    )