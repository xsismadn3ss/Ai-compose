import reflex as rx
import time

class ToneMakerState(rx.State):
    note: str = "_"
    tone: str = "_"
    is_error: bool = False
    is_loaded: bool = False
    data: str = ''

    def set_note(self, note: str):
        self.note = note.upper()

    def set_tone(self, tone: str):
        self.tone = tone

    def clear(self):
        self.reset()
        self.is_loaded = False

    def generate_tone(self):
        if self.note == '_' or self.tone == '_':
            self.is_error = True
            self.is_loaded = False
            return

        self.data = f"{self.note} {self.tone}"
        time.sleep(0.2)
        self.is_loaded=True
        self.is_error=False
        return
    