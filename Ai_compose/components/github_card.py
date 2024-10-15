import reflex as rx
import requests


def github_card(username: str, description: str = "") -> rx.Component:
    github_data = requests.get(f"https://api.github.com/users/{username}").json()
    
    if 'html_url' in github_data:
        name = github_data["name"]
        url = github_data["html_url"]
        if len(name) > 10:
            name = name[0:10] + "..."
        avatar = rx.avatar(
            src=github_data["avatar_url"],
            radius='full',
            size='7',
            margin_bottom='0.5rem'
        )

    else:
        url = f"https:/github.com/{username}"
        name = ''
        avatar = rx.avatar(
            fallback=f"{username[0:2]}".upper(),
            size='7',
            radius='full',
            margin_bottom='0.5rem'
        )

    return rx.card(
        rx.link(
            rx.vstack(
                avatar,
                rx.color_mode_cond(
                    rx.text(name, size="3", weight="bold", color="#202020"),
                    rx.text(name, size="3", weight="bold", color="#d1d1d1"),
                ),
                rx.color_mode_cond(
                    rx.text(
                        "@" + username, size="1", weight="regular", color="#202020"
                    ),
                    rx.text(
                        "@" + username, size="1", weight="regular", color="#d1d1d1"
                    ),
                ),
                rx.color_mode_cond(
                    rx.text(
                        description,
                        size="2",
                        weight="medium",
                        color="#202020",
                        margin_top="0.6rem",
                    ),
                    rx.text(
                        description,
                        size="2",
                        weight="medium",
                        color="#d1d1d1",
                        margin_top="0.6rem",
                    ),
                ),
                align="center",
                spacing="0",
            ),
            href=url,
        ),
        width="12rem",
        size="3",
    )
