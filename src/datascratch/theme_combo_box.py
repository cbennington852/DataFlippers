import PyQt5.QtWidgets as QtW
from qfluentwidgets import ComboBox
import matplotlib.pyplot as plt

class ThemeComboBox(ComboBox):

    CURRENT_THEME = "default"

    def __init__(self, parent=None):
        super().__init__(parent)
        available_styles = plt.style.available
        self.addItems(available_styles)
        self.setCurrentIndex(0)
        self.currentIndexChanged.connect(self.update_theme)


    def update_theme(self , i):
        new_theme = self.itemText(i)
        plt.style.use("default")
        ThemeComboBox.CURRENT_THEME = new_theme
        plt.style.use(ThemeComboBox.CURRENT_THEME)