import reflex as rx
import requests


def github_card(username: str, description: str = "") -> rx.Component:
    try:
        github_data = requests.get(f"https://api.github.com/users/{username}").json()
        profile_image = github_data["avatar_url"]
        name = github_data["name"]
        url = github_data["html_url"]
        if len(name) > 10:
            name = name[0:10] + "..."
    except Exception as e:
        url = f"https:/github.com/{username}"
        name = None

    return rx.card(
        rx.link(
            rx.vstack(
                rx.avatar(
                    src=profile_image,
                    fallback=f"{username[0:2]}".upper(),
                    radius="full",
                    size="7",
                    margin_bottom="0.5rem",
                ),
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
