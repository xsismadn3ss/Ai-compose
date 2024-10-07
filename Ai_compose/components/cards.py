import reflex as rx

def card():
    return rx.grid(
        rx.card("Generador de Acordes", background_color='#8348FF'),
        rx.card("Generador de Escalas y Tonalidades", background_color="#8348FF"),
        rx.card("Chat", background_color='#8348FF'),
        rx.card("Documentación", background_color='#8348FF'),
        spacing="2",
        columns="4",
        height="20vh",
        margin="5vh 5vh 10vh",
    )
    