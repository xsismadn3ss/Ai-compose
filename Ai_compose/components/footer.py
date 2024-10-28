import reflex as rx

def footer():
    return rx.flex(
        rx.divider(color="pink", margin_bottom='2rem'),
        rx.flex(
            rx.text("© 2024 AiCompose.", weight='bold'),
            rx.text('Todos los derechos reservados.', weight='regular'),
            spacing='2'
        ),
        rx.logo(),
        direction="column",
        justify='center',
        align='center',
        position="absolute",
        width='100%',
        bottom="0",
        padding_top='2rem',
        padding_bottom='1rem',
        padding_x='2rem'
    )
