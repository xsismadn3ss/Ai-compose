import reflex as rx

def login_form():
    return rx.dialog.content(
        rx.flex(
            rx.card(
                rx.flex(
                    rx.icon("music-2"), rx.heading(" Ai Compose"),
                    direction="row",                      
                ),
            ),
            rx.heading("Ingresa tus credenciales", as_="h4"),
            direction="column",
            align="center",
            spacing="2"          
        ),
        rx.flex(
            rx.text("Username", weight="bold", margin_top="1vh"), rx.input(placeholder="Ingresa tu nombre de usuario"),
            rx.text("Email", weight="bold"), rx.input(placeholder="correo@example.com"),
            rx.text("Password", weight="bold"), rx.input(placeholder="Ingresa tu contraseña"),
            rx.link("¿No tienes una cuenta? Registrate aquí", href="/sign_up", size="2", color_scheme='purple'),
            spacing="4",
            direction="column",
            margin="auto 2vh 2vh"
        ),
        rx.dialog.close(
            rx.flex(
                rx.button("Cancelar"),
                rx.button("Ingresar"),
                justify="center",
                spacing="3"
            ),
        ),
        width="30vw",
        padding="2em",
        max_width="28em",
    )