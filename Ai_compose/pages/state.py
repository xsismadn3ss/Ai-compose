# state.py
import reflex as rx
import asyncio
from g4f.client import Client

client = Client()


class State(rx.State):
    question: str = ""
    chat_history: list[tuple[str, str]] = []

    def clear_history(self):
        self.chat_history = []
        return rx.toast.success("Iniciando un a nueva conversación")

    def answer(self):

        if self.question == "":
            return rx.toast.error("Asegurate de escribir algo antes de comenzar", position='top-center')

        session = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": self.question
                    + "responde unicamente en español, y trata de responder todo unicamente relacionado a teoria musical",
                }
            ],
            stop=None,
            temperature=0.5,
            stream=True,
        )

        answer = ""
        self.chat_history.append((self.question, answer))

        self.question = ""
        yield

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (
                    self.chat_history[-1][0],
                    answer,
                )
        yield
