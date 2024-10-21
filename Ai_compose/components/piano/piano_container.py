import reflex as rx
from rxconfig import piano_style

def piano(*notes: rx.Component, style: dict = piano_style):
    return rx.flex(notes, style=style)