from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QMimeData, QPoint


class FakeDropEvent():
    def __init__(self , widget : QWidget):
        self.widget = widget
    def accept(self):
        pass
    def reject(self):
        pass
    def source(self) -> QWidget:
        return self.widget
    def pos(self) -> QPoint:
        return QPoint(0,0)
    
    
    # For the purpose of simulation
    def simulate(widget_receiving : QWidget,  widget_dropped : QWidget):

        fake_event = FakeDropEvent(
            widget_dropped
        )
        widget_receiving.dragEnterEvent(fake_event)
        widget_receiving.dropEvent(fake_event)
        widget_receiving.repaint()
        widget_receiving.dragLeaveEvent(fake_event)