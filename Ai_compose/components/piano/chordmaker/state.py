import reflex as rx
import time
from ....API.api_config import chords


class ChordMakerState(rx.State):
    note: str = "_"
    symbol: str = "_"
    is_error: bool = False
    is_loaded: bool = False
    notes: list[str] = []
    data: dict

    def set_note(self, note: str):
        self.note = note.upper()

    def delete_note(self):
        self.note = "Selecciona una nota"

    def set_symbol(self, symbol: str):
        self.symbol = symbol

    def clear(self):
        self.reset()
        self.is_loaded = False

    def generate_chord(self):
        if self.note == "_" or self.symbol == "_":
            self.is_error = True
            self.is_loaded = False
            return

        response = chords.generate(note=self.note, symbol=self.symbol)
        self.data = response
        self.notes = response['notes']
        time.sleep(0.2)
        self.is_loaded = True
        self.is_error = False
        return

    @rx.var
    def get_data(self):
        return self.note
