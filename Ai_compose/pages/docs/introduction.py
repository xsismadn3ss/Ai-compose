import reflex as rx
from ...templates.master import template


@rx.page(route='docs/', title='Documentación')
@template
def introduction():

    with open('docs\Música.md', encoding='utf-8') as readme:
        content = readme

    return rx.container(
        rx.card(rx.markdown(content), size='3'),
        justify='center',
        direction='column'
    )