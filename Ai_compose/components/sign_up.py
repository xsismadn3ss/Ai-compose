import reflex as rx

def signup_form() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.icon("music-2"),
                rx.heading("Bienvenido a Ai Compose"),
                rx.heading(
                    "Crea una cuenta",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Username",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="Ingresa tu username",
                    type="text",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Email",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="correo@ejemplo.com",
                    type="email",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Nombres",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Ingresa tus nombres",
                        type="text",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ), 
                
                rx.vstack(
                    rx.text(
                        "Apellidos",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Ingresa tus apellidos",
                        type="text",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
            ),
            rx.vstack(
                rx.text(
                    "Password",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="Ingresa tu contraseña",
                    type="password",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Confirmar contraseña",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="Confirma tu contraseña",
                    type="password",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.button("Registrarse", size="3", width="100%"),
            rx.center(
                rx.text("¿Ya estás registrado?", size="3"),
                rx.link("Logéate", href="#", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="60rem",
        margin_top="5vh"
    )