from PyQt5.QtWidgets import QWidget , QVBoxLayout
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg , NavigationToolbar2QT


class CanvasWithToolbar(QWidget):

    # Change it to be where we render the figure using SVG's
    # Using an PyQt image instead of this awful QTAgg backend.
    # This image should be temporary and have try catch finally to ensure it is removed. 

    def __init__(self , fig , **kwargs):
        super().__init__(**kwargs)
        self.my_layout = QVBoxLayout()
        self.setLayout(self.my_layout)

        self.canvas = FigureCanvasQTAgg(fig)
        self.toolbar = NavigationToolbar2QT(self.canvas , self)

        self.my_layout.addWidget(self.toolbar)
        self.my_layout.addWidget(self.canvas)
