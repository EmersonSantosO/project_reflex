import reflex as rx


def index() -> rx.Component:
    return rx.container(
        rx.box(
            "Hello world!",
            text_align="right",
        ),
        rx.box(
            "Hello world!",
            text_align="left",

        )
    )


def qa(question: str, answer: str) -> rx.Component:
    return rx.container(
        rx.box(
            question,
            text_align="right",
        ),
        rx.box(
            answer,
            text_align="left",
            margin_y="1em"

        )
    )


app = rx.App()
app.add_page(index)
app.compile()
