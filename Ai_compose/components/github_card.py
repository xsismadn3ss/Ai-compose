import reflex as rx
import requests

def github_card(username: str, description:str="")-> rx.Component:
    github_data = requests.get(f"https://api.github.com/users/{username}").json()
    url = github_data["html_url"]
    profile_image = github_data["avatar_url"]
    name = github_data['name']
    
    if len(name) > 10:
        name = name[0:10] + '...'
        
    return rx.card(
        rx.link(
            rx.vstack(
                rx.avatar(src=profile_image, radius="full", size="7", margin_bottom='0.5rem'),
                rx.color_mode_cond(
                    rx.text(name, size="3", weight="bold", color="#202020"),
                    rx.text(name, size="3", weight="bold", color="#d1d1d1"),
                ),
                rx.color_mode_cond(
                    rx.text('@'+username, size="1", weight="regular", color="#202020"),
                    rx.text('@'+username, size="1", weight='regular', color="#d1d1d1"),
                ),
                rx.color_mode_cond(
                    rx.text(description, size="2", weight='medium', color="#202020", margin_top="0.6rem"),
                    rx.text(description, size="2", weight='medium', color="#d1d1d1", margin_top='0.6rem'),
                ),
                align="center",
                spacing='0'
            ),
            href=url,
        ),
        width="12rem",
        size="3"
    )