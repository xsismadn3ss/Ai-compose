import reflex as rx

@rx.page(route="/about", title="About")
def about():
    return rx.text("About")