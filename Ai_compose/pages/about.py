import reflex as rx

@rx.page(route="/about", title="About")
def about():
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.vstack(
        rx.color_mode.button(position="top-right"),
        rx.markdown(content)
    )