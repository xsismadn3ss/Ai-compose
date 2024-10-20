import reflex as rx
from ....API.api_config import chords


class ChordMakerState(rx.State):
    note: str = "_"
    symbol: str = "_"

    def set_note(self, note: str):
        self.note = note.upper()

    def delete_note(self):
        self.note = "Selecciona una nota"

    def set_symbol(self, symbol: str):
        self.symbol = symbol

    def clear(self):
        self.reset()

    def generate_chord(self):
        if self.note == "_" or self.symbol == "_":
            return rx.toast.error(
                "Asegurate de seleccionar una nota y una proporción antes de generar un acorde",
                position="top-center",
            )

        response = chords.generate(note=self.note, symbol=self.symbol)

        return rx.toast.info(
            " Generando acorde {} {}, Acorde: {}".format(
                self.note, self.symbol, response
            ),
            position="top-center",
        )

    @rx.var
    def get_data(self):
        return self.note
