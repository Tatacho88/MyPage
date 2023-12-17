import reflex as rx



def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
              name="Jeison Santamaria"
            ),
            rx.text("Jeison Santamaria"),
            rx.spacer(),
            width="100%"
        )
    )