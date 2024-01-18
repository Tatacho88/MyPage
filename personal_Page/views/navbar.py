import reflex as rx
import personal_Page.constants as constants
from personal_Page.styles.styles import Color, Size
from personal_Page.components.link_icon import link_icon

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
              name="Jeison Santamaria"
            ),
            rx.text("Jeison Santamaria"),
            rx.spacer(),
            link_icon(
                "facebook",
                constants.FACEBOOK_URL
            ),
            link_icon(
                "instagram",
                constants.INSTAGRAM_URL
            ),
            link_icon(
                "github",
                constants.GITHUB_URL
            ),
            width="100%"
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )