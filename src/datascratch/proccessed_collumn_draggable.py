from PyQt5.QtWidgets import QVBoxLayout
import PyQt5.QtWidgets as QtW
from PyQt5.QtCore import QMimeData, QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDrag , QPixmap , QPainter , QPalette , QImage , QColor , QPolygon, QPen, QBrush, QIcon
from datascratch.column_pipeline import ColumnsSection
import pandas as pd
from datascratch.draggable_pipeline import PipelineSection
from datascratch.list_of_acceptable_sklearn_functions import SklearnAcceptableFunctions

class PreProcessorColumn(QtW.QWidget):

    def __init__(self , dataframe : pd.DataFrame, **kwargs):
        super().__init__(**kwargs)
        self.dataframe = dataframe
        self.column_droppable_flag = True
        self.my_layout = QtW.QVBoxLayout()
        self.setLayout(self.my_layout)

        # 1. A drop port for the pre-proccessor
        PREPROCESSOR_FILTER = lambda x : x in SklearnAcceptableFunctions.PREPROCESSORS
        self.pre_processor_port  = PipelineSection(
            title="Preprocessor",
            accepting_function=PREPROCESSOR_FILTER,
            my_parent=self
        )

        # 2. A drop port for the columns
        self.column_port = ColumnsSection(
            "Any Column",
            self,
            dataframe,
            1
        )

        self.my_layout.addWidget(self.pre_processor_port)
        self.my_layout.addWidget(self.column_port)

    def copy_self(self):
        return PreProcessorColumn(self.dataframe)


    def mouseMoveEvent(self, e):
        # Makes it draggable
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            # Render this while dragging
            pixmap = QPixmap(self.size())
            # Tell the button to drag in the center.
            drag.setHotSpot(self.drag_start_position) 
            #drag.setHotSpot(center)
            self.render(pixmap)
            drag.setPixmap(pixmap)

            drag.setMimeData(mime)
            drag.exec_(Qt.MoveAction)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
        super(PreProcessorColumn, self).mousePressEvent(event)