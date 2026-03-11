import PyQt5.QtWidgets as QtW
import traceback
import PyQt5.QtCore as QtCore 
import pandas as pd
import matplotlib.pyplot as plt

from qfluentwidgets import ScrollArea , ListWidget , ListView
from datascratch.theme_combo_box import ThemeComboBox

from datascratch.canvas_with_toolbar import CanvasWithToolbar



class NumericalDescriptor(QtW.QWidget):

    def __init__(self, column_name : str ,  dataframe : pd.DataFrame, **kwargs):
        """
        Shows the numerical statistics in the form of a bar chart + other things! 
        """
        super().__init__(**kwargs)
        self.column_name = column_name
        self.dataframe = dataframe

        self.my_layout = QtW.QVBoxLayout()
        self.setLayout(self.my_layout)

        # Bar Chart
        col = self.dataframe[self.column_name]
        fig, axs = plt.subplots(figsize=(4 ,4))
        axs.hist(col)
        axs.set_ylabel("Frequency")
        axs.set_xlabel(f"{self.column_name} values")
        self.chart = CanvasWithToolbar(fig)


        # A list of stats about this bar chart


        # Settle appearance
        self.my_layout.addWidget(self.chart)

        

class CategoricalDescriptor(QtW.QWidget):

    def __init__(self, column_name : str ,  dataframe : pd.DataFrame, **kwargs):
        """
        Shows the numerical statistics in the form of a bar chart + other things! 
        """
        super().__init__(**kwargs)
        self.column_name = column_name
        self.dataframe = dataframe

        self.my_layout = QtW.QVBoxLayout()
        self.setLayout(self.my_layout)

        value_counts = dataframe[column_name].value_counts()
        names = value_counts.index.tolist()
        
        fig, axs = plt.subplots(figsize=(4 ,4))
        axs.pie(value_counts, labels=names, autopct='%1.1f%%', startangle=90) 
        self.chart = CanvasWithToolbar(fig)


        # Settle appearance
        self.my_layout.addWidget(self.chart)