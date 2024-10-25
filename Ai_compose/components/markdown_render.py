import reflex as rx


def markdown(path: str = ""):
    with open(path, encoding="utf-8") as mk:
        content = mk.read

    return rx.markdown(content)
