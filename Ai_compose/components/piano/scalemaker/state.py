import reflex as rx
from g4f.client import Client
import time


class ScaleMakerState(rx.State):
    note: str = "_"
    is_error: bool = False
    is_loaded: bool = False
    data: str = ""

    def set_note(self, note: str):
        self.note = note.upper()

    def clear(self):
        self.reset(),
        self.is_loaded = False

    def ask_gpt(self):
        format_output = """ En base a la nota selecionada las escalas que puedes utilizar son:

        * **Escala mayor**: se compone por las notas ...
        * **Escala menor**: se compone por las notas ...
        * **Escala pentatonica**: se compone por las notas ...
        * **Escala de blues**: se compone por las notas ...
        * **Escala de jazz**: se compone por las notas ...
        """

        prompt = f"""En base a la nota {self.note}, muestrame su escala mayor, escala menor y escala pentatonica. Por favor sigue este formato para responder: {format_output}
        """
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    def generate_scale(self):
        if self.note == "_":
            self.is_error = True
            self.is_loaded = False
            return

        self.data = self.ask_gpt()
        time.sleep(0.2)
        self.is_loaded = True
        self.is_error = False
        return
