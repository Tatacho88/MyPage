import reflex as rx
from personal_Page.styles.styles import Size

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Esta web esta creada completamente en Reflex",
            size="lg",
            padding_botom=Size.DEFAULT.value
        ),
        rx.flex(
            rx.image(
                src= "fotoamore.png",
                alt= "foto con mi esposa",
                width="16em",
                height="16em",
                margin_right=Size.BIG.value
            ),
            rx.vstack(
                rx.box(
                    rx.text(""),
                    rx.span(),
                    rx.span()
                )
            )
        )
    )