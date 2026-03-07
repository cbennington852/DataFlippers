import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from qfluentwidgets import FluentWindow, setTheme, Theme


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("homePage")   # REQUIRED

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Home Page"))


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("settingsPage")   # REQUIRED

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Settings Page"))


class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        self.homePage = HomePage()
        self.settingsPage = SettingsPage()

        self.addSubInterface(self.homePage, "home", "Home")
        self.addSubInterface(self.settingsPage, "settings", "Settings")

        self.resize(800, 600)


app = QApplication(sys.argv)
setTheme(Theme.DARK)

w = Window()
w.show()

sys.exit(app.exec())