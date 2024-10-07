import reflex as rx
from .login_form import login_form

def icon_button(icon_name: str):
    return rx.icon(icon_name)

    
def navbar_link(text: str, url: str):
    return rx.link(
        rx.text(text, size="3", weight="medium"), href=url
    )
    
def signup_button(): 
    return rx.dialog.root(
       rx.dialog.trigger(
            rx.button("Comienza a aprender")
       ),
       login_form(),
    )

    
def login_button():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.icon_button(
                rx.icon("user"),
                size="2",
                radius="full",
            )       
        ),
        login_form()
    )
    
def navbar()-> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.flex(
                rx.center(
                    rx.box(
                        rx.icon("music-2"),
                        radius="full",
                        padding="1rem"
                    ),
                    rx.heading("Ai Compose", as_="h2"),     
                    spacing="3",         
                ),
                rx.center(
                    navbar_link("Home", "/"),
                    navbar_link("Piano Roll", "/piano_roll"),
                    navbar_link("Documentación", "/#"),
                    rx.link(rx.button("Chat", rx.icon("message-circle-more"), size="3", variant="outline"), href="/chat"), 
                    login_button(),                  
                    rx.color_mode.button(),
                    spacing="4",
                    margin="1vh 0",
                ),
                spacing="8",
                justify="between",
                direction="row",
            ),
            rx.divider(),
        )
    )