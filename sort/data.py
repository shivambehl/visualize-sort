class Data:
    data_count = 32
    color = (0, 0, 0, 0)

    def __init__(self, value):
        self.value = value
        self.set_color()

    def set_color(self, rgba=None):
        if not rgba:
            rgba = (
                0.2,
                1 - self.value / (self.data_count * 4),
                self.value / (self.data_count * 4) + 0.5,
                1
            )

        self.color = rgba
