import reflex as rx
from ....API.api_config import chords

class ChordMakerState(rx.State):
    note: str = "_"
    symbol: str = "#"

    def set_note(self, note: str):
        self.note = note.upper()

    def delete_note(self):
        self.note = "Selecciona una nota"

    def set_symbol(self, symbol: str):
        self.symbol = symbol

    def clear(self):
        self.note = "_"
        self.symbol = "#"

    def generate_chord(self):
        # TODO: agregar opción peticion y devolver un dialogo en vez de un toast
        response = chords.generate(note='C', symbol='maj7')
        return rx.toast.info(
            " Generando acorde {} {}, Acorde: {}".format(self.note, self.symbol, response),
            position="top-center",
        )

    @rx.var
    def get_data(self):
        return self.note