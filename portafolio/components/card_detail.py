import reflex as rx
from portafolio.data import Extra

from portafolio.styles.styles import IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover",
                    mb=12
                ),
                pb="current"
            ),
            rx.text.strong(extra.title, mt="10px"),
            rx.text(
                extra.description,
                size=Size.SMALL.value,
                color_scheme="gray",
                mt="10px"
            )
        ),
        width="100%",
        href=extra.url,
        is_external=True
    )
