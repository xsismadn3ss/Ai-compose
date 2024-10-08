import reflex as rx
import requests

def github_card(username: str)-> rx.Component:
    github_data = requests.get(f"https://api.github.com/users/{username}").json()
    url = github_data["html_url"]
    profile_image = github_data["avatar_url"]
    name = github_data['name']
    
    if len(name) > 10:
        name = name[0:10] + '...'
        
    return rx.card(
        rx.link(
            rx.vstack(
                rx.avatar(src=profile_image, radius="full", size="7"),
                rx.color_mode_cond(
                    rx.text(name, size="3", weight="bold", color="#202020"),
                    rx.text(name, size="3", weight="bold", color="#d1d1d1"),
                ),
                rx.color_mode_cond(
                    rx.text('@'+username, size="1", weight="medium", color="#202020"),
                    rx.text('@'+username, size="1", weight='medium', color="#d1d1d1"),
                ),
                align="center",
            ),
            href=url,
        ),
        width="12rem",
        size="3"
    )