import reflex as rx

def container(*args):
    return rx.container(
        args,
        justify='center',
        direction='column'
    )