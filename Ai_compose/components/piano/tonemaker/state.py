import reflex as rx
from g4f.client import Client
import time


class ToneMakerState(rx.State):
    note: str = "_"
    tone: str = "_"
    is_error: bool = False
    is_loaded: bool = False
    data: str = ""

    def set_note(self, note: str):
        self.note = note.upper()

    def set_tone(self, tone: str):
        self.tone = tone

    def clear(self):
        self.reset()
        self.is_loaded = False

    def ask_gpt(self):
        format_output = """En la tonalidad de [Nota] [Tono], los acordes principales suelen ser los siguientes:
        1. **####** (I): Formado por las notas ...
        2. **####** (II): Formado por las notas ...
        3. **####** (III): Formado por las notas ...
        4. **####** (IV): Formado por las notas ...
        5. **####** (V): Formado por las notas ...
        6. **####** (VI): Formado por las notas ...
        7. **####** (VII): Formado por las notas ...
        Estos son los acordes diatónicos principales dentro de la tonalidad de [Nota] [Tono]."""

        prompt = f"En base a teoría musical. Cuales son los acordes que conforman la tonalidad {self.note} {self.tone}. por favor sigue este formato {format_output}"
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

    def generate_tone(self):
        if self.note == "_" or self.tone == "_":
            self.is_error = True
            self.is_loaded = False
            return

        self.data = self.ask_gpt()
        time.sleep(0.2)
        self.is_loaded = True
        self.is_error = False
        return
