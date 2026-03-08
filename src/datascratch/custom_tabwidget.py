import PyQt5.QtWidgets as QtW


class CustomTabView(QtW.QTabWidget):
    def __init__(
        self, **kwargs
    ):
        super().__init__(**kwargs)
