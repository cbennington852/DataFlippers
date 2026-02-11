import PyQt5.QtWidgets as QtW
from PyQt5.QtGui import QKeyEvent 
from PyQt5.QtCore import Qt, QEvent

class CustomTextEditor(QtW.QTextEdit):
    def __init__(self, parent , **kwargs):
        super().__init__( **kwargs)
        self.my_parent = parent
        self.setLineWrapMode(QtW.QTextEdit.WidgetWidth)

    def keyPressEvent(self, event: QKeyEvent):
        # Example: Map Ctrl+S to a custom action
        if event.key() == Qt.Key.Key_B and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.my_parent.bold_button.click()
        else:
            # Standard behavior for other keys
            super().keyPressEvent(event)


class CustomEditorButton(QtW.QPushButton):
    def __init__(self, text_edit , function_to_apply , custom_style , **kwargs):
        """Custom buttons for the text editor.

        Args:
            text_edit (_type_): ptr to the text editor
            function_to_apply (_type_): function(bool_is_enabled, ptr_to_text_editor)
            custom_style (_type_): _description_
        """
        super().__init__( **kwargs)
        self.custom_style = custom_style
        self.text_edit = text_edit
        self.function_to_apply = function_to_apply
            # lambda function to take in bool + ptr to text_edit
        self.button_enabled = False

    def style_button(self):
        if self.button_enabled:
            self.text_edit.setFontWeight(NotesSubwindow.BOLD_FONT_WEIGHT)
            self.bold_button.setStyleSheet(f"background-color: black; color:white; {self.custom_style}")
        else:
            self.text_edit.setFontWeight(NotesSubwindow.NORMAL_FONT_WEIGHT)
            self.bold_button.setStyleSheet(f"background-color: white; color:black; {self.custom_style}")
        self.function_to_apply(self.button_enabled , self.text_edit)

    def setBold(self):
        self.button_enabled = not self.button_enabled
        self.style_button()


class NotesSubwindow(QtW.QMdiSubWindow):
    BASE_HEIGHT = 300
    BASE_WIDTH = 400

    BOLD_FONT_WEIGHT = 600
    NORMAL_FONT_WEIGHT = 300

    def __init__(self, parent , **kwargs):
        super().__init__(parent, **kwargs)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint , True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint , False)
        self.resize(NotesSubwindow.BASE_WIDTH , NotesSubwindow.BASE_HEIGHT)
        self.cursor_bold = False

        # Adding a text editor
        self.my_layout = QtW.QVBoxLayout()
        self.main_box = QtW.QWidget()
        self.main_box.setLayout(self.my_layout)

        self.text_edit = CustomTextEditor(self)


        # Adding a small toolbar
        self.tool_bar = QtW.QToolBar()

        def bold_func(is_enabled, tmp_editor_ptr):
            if is_enabled:
                tmp_editor_ptr.setFontWeight(NotesSubwindow.BOLD_FONT_WEIGHT)
            else:
                tmp_editor_ptr.setFontWeight(NotesSubwindow.NORMAL_FONT_WEIGHT)


        self.bold_button = CustomEditorButton(
            text_edit=self.text_edit,
            function_to_apply=bold_func,
            custom_style="font-weight: bold;"
        )
        self.tool_bar.addWidget(self.bold_button)


        # Order
        self.my_layout.addWidget(self.tool_bar)
        self.my_layout.addWidget(self.text_edit)
        self.setWidget(self.main_box)
