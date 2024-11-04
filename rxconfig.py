import reflex as rx

config = rx.Config(
    app_name="Ai_compose",
)

# estilos para teclas negras
black_keys_style = {
    "bg": "#303030",
    "border_radius": "0.5em",
    "margin_x": "0.4em",
    "margin_bottom": "0.4em",
}

# estilos para teclas blancas
white_keys_style = {
    "bg": "#f4eaff",
    "border_radius": "0.5em",
    "margin_x": "0.2em",
    "color": "#202020",
    "height": "4.2rem"
}

piano_style = {
    "flex_direction": "column",
    "margin_top": "0.5em",
    "border_radius": "1em",
    "padding": "0.6em",
    "bg": "linear-gradient(80deg, #3a353e, #5a3737, #402b50, #762242, #3a353e)",
    "justify": "center",
    "align": "center",
    "box_shadow": "0px 0px 50px #924337",
}

# efecto neón
glow_bg_light = {
    'box_shadow': '0px 0px 4.5rem 1rem #9563ee',
}

light_border = "1px solid #d3d3d3"
dark_border = "1px solid #414141"

# fondo transparente
bg_transparent_light = {
    "background": "transparent",
    "backdrop_filter": "blur(15px)",
    "background_image": """linear-gradient(
        180deg, 
        rgba(207, 191, 255, 0.8), 
        rgba(207, 191, 255, 0.8), 
        rgba(255, 255, 255, 0.8),
        rgba(255, 255, 255, 0.8)
    )
    """,
}

bg_transparent_light2 = {
    "background": "transparent",
    "backdrop_filter": "blur(15px)",
    "background_image": """linear-gradient(
        180deg, 
        rgba(207, 191, 255, 0.8), 
        rgba(255, 255, 255, 0.999)
    )
    """,
}

bg_transparent_dark = {
    "background": "transparent",
    "backdrop_filter": "blur(20px)",
}
