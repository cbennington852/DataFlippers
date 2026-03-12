import PyQt5.QtWidgets as QtW
import traceback
import PyQt5.QtCore as QtCore 
import pandas as pd
import matplotlib.pyplot as plt

from qfluentwidgets import ScrollArea , ListWidget , ListView , TableWidget
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

        self.my_layout = QtW.QHBoxLayout()
        self.setLayout(self.my_layout)

        # Bar Chart
        col = self.dataframe[self.column_name]
        fig, axs = plt.subplots(figsize=(4 ,4))
        axs.hist(col)
        axs.set_ylabel("Frequency")
        axs.set_xlabel(f"{self.column_name} values")
        axs.set_title(f"Single Series Column Chart for {self.column_name} ")
        self.chart = CanvasWithToolbar(fig)

        

        # Resolve the statistical parts for this.
        list_of_pairs = [
            ('Mean' , col.mean()),
            ('Median' , col.median()),
            ('Variance' , col.var()),
            ('Max' , col.max()),
            ('Min' , col.min()),
            ('75th percentile' , col.quantile(0.75)),
            ('50th percentile' , col.quantile(0.50)),
            ('25th percentile' , col.quantile(0.25)),
        ]

        # A list of stats about this bar chart
        self.list_stats = TableWidget(self)
        self.list_stats.setRowCount(len(list_of_pairs))
        self.list_stats.setColumnCount(2)
        self.list_stats.setHorizontalHeaderLabels(["Stat" , "Value"])
        self.list_stats.verticalHeader().hide()

        for k in range (0 , len(list_of_pairs)):
            ir_value = str(round(list_of_pairs[k][1] , 4))
            print(ir_value , "Curr " , k)
            self.list_stats.setItem( k ,0 , QtW.QTableWidgetItem(list_of_pairs[k][0]))
            self.list_stats.setItem( k ,1 , QtW.QTableWidgetItem(ir_value))

        # Settle appearance
        self.my_layout.addWidget(self.chart)
        self.my_layout.addWidget(self.list_stats)


        

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
        axs.set_title(f"Distribution for {self.column_name}")
        self.chart = CanvasWithToolbar(fig)


        # Settle appearance
        self.my_layout.addWidget(self.chart)