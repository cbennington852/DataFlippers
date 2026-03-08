from PyQt5 import QtWidgets as QtW
from qfluentwidgets import FluentWindow, setTheme, Theme
from qfluentwidgets import PushButton
from PyQt5.QtGui import QDrag , QPixmap , QPainter , QPalette , QImage , QColor , QPolygon, QPen, QBrush, QIcon 
from PyQt5.QtCore import QPoint


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
    CardWidget , ElevatedCardWidget
)

from qfluentwidgets import CommandBar, Action, FluentIcon as FIF
from PyQt5.QtCore import Qt, QMimeData



class CustomMDI(QtW.QMdiSubWindow):

    CUSTOM_MDI_WINDOW_STYLING = """
        CustomMDI , Plotter , NotesSubwindow {
            background: transparent;
        }
    """

    def __init__(self, parent):
        super().__init__(parent=parent)
        
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        
        
        # TODO:
            # 1. Overide the drag and drop and replace with own bar
            # 2. Replace close with own, controllabel closer
            # 3. Minimise not required but could be nice

        # Toolbar
        self.main = CardWidget()
        self.toolbar = DragTopBar(self) # MDI window is parent
        self.my_layout = QtW.QVBoxLayout()
        self.my_layout.setContentsMargins(0 , 0, 0 , 0)
        self.my_layout.setSpacing(0)

        self.main.setLayout(self.my_layout)
        self.setWidget(self.main)

        #   Closer button
        self.close_button = ToolButton(FluentIcon.CLOSE , self.toolbar)
        self.close_button.setStyleSheet("""
            ToolButton {
                border-radius : 15px;
            }
            ToolButton:hover  {
                background-color: red;   
                border-radius : 15px;
            }
        """)
        self.close_button.setContentsMargins(0,0,15,0)
        self.close_button.clicked.connect(self.close)
    

        self.content = QtW.QWidget()
        self.content_layout = QtW.QVBoxLayout()
        self.content.setLayout(self.content_layout)
        self.toolbar.addWidget(self.close_button)
        self.my_layout.addWidget(self.toolbar)
        self.my_layout.addWidget(self.content)
        self.toolbar.setFixedHeight(self.toolbar.height())

       


    def disableClose(self):
        self.close_button.deleteLater()



class DragTopBar(QtW.QToolBar):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setStyleSheet("""
            background-color : darkgrey;
            border-top-left-radius : 10px;
            border-top-right-radius : 10px;               
        """)
        
        spacer = QtW.QWidget()
        spacer.setSizePolicy(QtW.QSizePolicy.Expanding , QtW.QSizePolicy.Expanding)
        self.addWidget(spacer)
        self.setMinimumWidth(200)
        self.my_parent = parent



    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_pos = event.globalPos()

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            delta = QPoint(e.globalPos() - self.last_pos)
            self.my_parent.move(self.my_parent.x() + delta.x() , self.my_parent.y() + delta.y())
            self.last_pos = e.globalPos()