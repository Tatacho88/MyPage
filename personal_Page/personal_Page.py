import reflex as rx
import personal_Page.styles.styles as styles
from personal_Page.views.navbar import navbar


def index() -> rx.Component:
    return rx.box(
        navbar()
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title="Jeison Santamaria",
    description="Esta es mi primera pagina web con Reflex"
)

app.compile()
