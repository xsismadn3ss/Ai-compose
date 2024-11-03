import reflex as rx

def feature_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon("check", color=rx.color("grass", 9)),
        rx.text(text, size="4"),
    )

def feature_list(features: list[str]) -> rx.Component:
    return rx.vstack(
        *(feature_item(feature) for feature in features),
        width="100%",
        align_items="start"
    )

def pricing_card(title: str, description: str, price: str, features: list[str]) -> rx.Component:
    return rx.vstack(
        rx.text(title, weight="bold", size="6"),
        rx.text(description, size="4", opacity=0.8, align="center"),
        rx.hstack(
            rx.text(price, weight="bold", font_size="3rem", trim="both"),
            rx.text("/month", size="4", opacity=0.8, trim="both"),
            width="100%",
            align_itmes="end",
            justify="center",
        ),
        feature_list(features),
        rx.button("Comenzar", size="3", variant="solid", width="100%"),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        justify="cemter",
        border_radius="0.5rem",
    )

basic_features = ["First Feature", "Second Feature", "Third Feature", "Fourth Feature"]  # Pull from database
advanced_features = ["First Feature", "Second Feature", "Third Feature", "Fourth Feature"]  # Pull from database
premium_features = ["First Feature", "Second Feature", "Third Feature", "Fourth Feature"]  # Pull from database

basic_card = pricing_card("Básico","Basic plan description","$precio", basic_features)
advanced_card = pricing_card("Avanzado", "Advanced plan description", "$precio", advanced_features)
premium_card = pricing_card("Premium", "Premium plan description","$precio", premium_features)