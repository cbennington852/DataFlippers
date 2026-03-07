from PyQt5.QtWidgets import QFileDialog, QStyle, QTableView, QApplication
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
import sys
from PyQt5.QtGui import *
import pandas as pd
import PyQt5.QtWidgets as QtW


from qfluentwidgets import StyleSheetBase, Theme, isDarkTheme, qconfig

from qfluentwidgets import FluentWindow, setTheme, Theme
from qfluentwidgets import PushButton

from qfluentwidgets import (
    PushButton, PrimaryPushButton, TransparentPushButton, ToolButton,
    RadioButton, CheckBox, SwitchButton, ComboBox, EditableComboBox,
    Slider, SpinBox, DoubleSpinBox, DateEdit, TimeEdit, DateTimeEdit,
    LineEdit, SearchLineEdit, PasswordLineEdit, TextEdit, PlainTextEdit,
    ProgressBar, ProgressRing,CaptionLabel, BodyLabel, 
    SubtitleLabel, TitleLabel, LargeTitleLabel, DisplayLabel,
    ScrollArea, SmoothScrollArea, HorizontalFlipView, VerticalFlipView,
    AvatarWidget, ImageLabel,  InfoBadge, DotInfoBadge, IconInfoBadge
)

from qfluentwidgets import (
    FluentWindow, MSFluentWindow, SplitFluentWindow, NavigationInterface,
    NavigationItemPosition, NavigationTreeWidget, NavigationBar, Pivot, SegmentedWidget, BreadcrumbBar
)

from qfluentwidgets import (
    ListWidget, ListView, TableWidget, TableView, TreeWidget, TreeView,
    FluentIcon, FluentIconBase, getIconColor, 
    Theme, setTheme, ThemeColor, setThemeColor, HeaderCardWidget
)


from qfluentwidgets import (
    SettingCard, SwitchSettingCard, RangeSettingCard, OptionsSettingCard,
    PrimaryPushSettingCard, PushSettingCard, HyperlinkCard, 
    SettingCardGroup, ExpandSettingCard, CustomColorSettingCard
)

from qfluentwidgets import CommandBar, Action, FluentIcon as FIF

class DataframeViewer(QtW.QWidget):
    def __init__(self, df, **kwargs):
        super().__init__(**kwargs)
        self.my_layout = QtW.QVBoxLayout()
        self.setLayout(self.my_layout)
        
        self.my_toolbar = QtW.QToolBar()

        # Save Button
        self.save_df_button = QtW.QPushButton("")
        save_icon = QIcon(":/images/filesave.svg")
        self.save_df_button.setIcon(save_icon)
        self.save_df_button.clicked.connect(self.save_clicked)
        self.my_toolbar.addWidget(self.save_df_button)

        self.dataframe_model = InternalDataframeViewer(df)

        self.my_layout.addWidget(self.my_toolbar)
        self.my_layout.addWidget(self.dataframe_model)

    def get_pd_dataframe(self) -> pd.DataFrame:
        return self.dataframe_model.model()._dataframe

    def save_clicked(self):
        file_name, selected_filter = QFileDialog.getSaveFileName(
            self, 
            "Save File", 
            "", # Start in current directory or specific path like "/home/user"
            ".csv;;.xls;;" # File filters separated by ';;'
        )

        # Check if a file name was selected (user didn't cancel)
        if file_name:
            try:
                # Manually save the content to the selected file path
                print("User file name: " , file_name)
                print("User file path" , selected_filter)
                with open(file_name, 'w') as f:
                    # check file ending
                    pd_df : pd.DataFrame = self.dataframe_model.model()._dataframe
                    if selected_filter == ".csv":
                        pd_df.to_csv(file_name + ".csv")
                    elif selected_filter == ".xls":
                        pd_df.to_excel(file_name + ".xls")
                    else:
                        raise Exception("Invalid file extension")
                print(f"File saved successfully to: {file_name}")
            except Exception as e:
                print(f"Error saving file: {e}")

class InternalDataframeViewer(TableView):
    """
    Small data frame class to view a dataframe.
    """
    def __init__(self, df, **kwargs):
        super().__init__(**kwargs)
        self.resize(800, 500)
        self.horizontalHeader().setStretchLastSection(True)
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QTableView.SelectRows)
        model = PandasModel(df)
        self.setModel(model)

    def save_dataframe(self, file_name):
        pass



class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """

    def __init__(self, dataframe: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0
    
    def setData(self, index, value, role):
        """This allows us to edit the pandas dataframe

        Return true, to say is was edited.
        """
        try:
            if role == Qt.EditRole:
                new_type = self._dataframe.iloc[index.row(),index.column()].dtype
                print("New type" , new_type)
                new_value = new_type.type(value)
                self._dataframe.iloc[index.row(),index.column()] = new_value
                return True
        except Exception as e:
            print(str(e))
            return False
        
        
    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._dataframe.iloc[index.row(), index.column()])

        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._dataframe.columns[section])

            if orientation == Qt.Vertical:
                return str(self._dataframe.index[section])

        return None
