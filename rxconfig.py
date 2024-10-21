import reflex as rx

config = rx.Config(
    app_name="Ai_compose",
)

#estilos para teclas negras
black_keys_style = {
    "bg": "#303030",
    "border_radius": "0.5em",
    "margin_x": "0.4em",
    "margin_bottom": "0.4em",
}

#estilos para teclas blancas
white_keys_style = {
    "bg": "#d1d1d1",
    "border_radius": "0.5em",
    "margin_x": "0.2em",
    "color": "#202020",
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

#efecto neón 
glow_bg_light = {
    'box_shadow': '0px 0px 4.5rem 1rem #9563ee',
}

light_border = "1px solid #d3d3d3"
dark_border = "1px solid #414141"