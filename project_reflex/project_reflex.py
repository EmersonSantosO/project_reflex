import reflex as rx


class State(rx.State):
    count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index():
    return rx.vstack(
        rx.hstack(
            rx.button("Decrement",
                      color_scheme="red",
                      border_radius="0.5em",),
            rx.heading(font_size="2em"),
            rx.button("Increment",
                      color_scheme="green",
                      border_radius="0.5em"
                      )


        )
    )


app = rx.App()
app.add_page(index)
app.compile()
