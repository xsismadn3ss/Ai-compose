import reflex as rx
from rxconfig import black_keys_style, white_keys_style, piano_style


# Estado
class pianoState(rx.State):
    data: list[str] = [""]
    payload: list[int] = []


    def add_note(self, note: str, position: int):
        self.data.append("{}".format(note))
        self.payload.append(position)

    def delete_note(self):
        try:
            if len(self.data) >= 1:
                self.data.pop()
                self.payload.pop()
        except Exception as e:
            return rx.toast.warning("Ya no hay mas notas que eliminar")

    def send_notes(self) -> rx.Component:
        if len(self.payload) >= 1:
            return rx.toast.success(
                "Enviado, generando respuesta\n({})".format(self.payload)
            )

        return rx.toast.warning("Ninguna nota ha sido enviada")

    def clear_notes(self):
        self.payload = []
        self.data = [""]
    
    @rx.var
    def get_data(self):
        return self.data


def black_key(note: str, position: int):
    return rx.button(
        note, style=black_keys_style, on_click=pianoState.add_note(note, position)
    )


def blackKeys():
    return (
        rx.flex(
            black_key("C#", 2),
            black_key("D#", 4),
            rx.button("", variant="ghost", margin_x="0.4em"),
            black_key("F#", 7),
            black_key("G#", 9),
            black_key("A#", 11),
            justify="center",
        ),
    )


def white_key(note: str, position: int):
    return rx.button(
        note,
        style=white_keys_style,
        size="3",
        on_click=pianoState.add_note(note, position),
    )


def whitekeys():
    return rx.flex(
        white_key("C", 1),
        white_key("D", 3),
        white_key("E", 5),
        white_key("F", 6),
        white_key("G", 8),
        white_key("A", 10),
        white_key("B", 12),
    )


def formButtons():
    return rx.flex(
        rx.button(
            "enviar",
            variant="soft",
            color_scheme="green",
            size="1",
            on_click=pianoState.send_notes(),
        ),
        rx.button(
            "eliminar",
            variant="soft",
            color_scheme="gray",
            size="1",
            on_click=pianoState.delete_note(),
        ),
        rx.button(
            "borrar",
            variant="soft",
            color_scheme="red",
            size="1",
            on_click=pianoState.clear_notes(),
        ),
        direction="row",
        justify="end",
        wrap="wrap",
    )


def piano_roll():
    return rx.flex(
        rx.text(pianoState.get_data, size="3", margin_y="0.8em", text_align="center"),
        formButtons(),
        rx.flex(
            blackKeys(),
            whitekeys(),
            style=piano_style
        ),
        margin_y="0.8em",
        direction="column",
    )
