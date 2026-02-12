import PyQt5.QtWidgets as QtW
from PyQt5.QtGui import QKeyEvent  , QFont
from PyQt5.QtCore import Qt, QEvent




class CustomTextEditor(QtW.QTextEdit):
    def __init__(self, parent , **kwargs):
        super().__init__( **kwargs)
        self.my_parent = parent
        self.setLineWrapMode(QtW.QTextEdit.WidgetWidth)
        self.setAutoFormatting(QtW.QTextEdit.AutoBulletList)

        self.cursorPositionChanged.connect(self.cursor_moved)

    def cursor_moved(self):
        self.my_parent.check_button_states()


    def keyPressEvent(self, event: QKeyEvent):
        # Example: Map Ctrl+S to a custom action
        if event.key() == Qt.Key.Key_B and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.my_parent.bold_button.click()
        elif event.key() == Qt.Key.Key_I and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.my_parent.italic_button.click()
        elif event.key() == Qt.Key.Key_U and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.my_parent.under_button.click()
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
        self.clicked.connect(self.switch_button)
        self.style_button()


    def style_button(self):
        if self.button_enabled:
            self.setStyleSheet(f"background-color: black; color:white; {self.custom_style}")
        else:
            self.setStyleSheet(f"background-color: white; color:black; {self.custom_style}")
        self.function_to_apply(self.button_enabled , self.text_edit)

    def switch_button(self):
        self.button_enabled = not self.button_enabled
        self.style_button()

class NotesData():
    def __init__(self , notes_text , x_pos , y_pos):
        self.notes_text = notes_text
        self.x_pos = x_pos
        self.y_pos = y_pos

class NotesSubwindow(QtW.QMdiSubWindow):
    BASE_HEIGHT = 300
    BASE_WIDTH = 400

    def __init__(self, parent , ptr_to_pipeline_parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.my_parent = ptr_to_pipeline_parent
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

        # Bold Button
        def bold_func(is_enabled, tmp_editor_ptr):
            if is_enabled:
                tmp_editor_ptr.setFontWeight(QFont.Bold)
            else:
                tmp_editor_ptr.setFontWeight(QFont.Normal)
        self.bold_button = CustomEditorButton(
            text_edit=self.text_edit,
            function_to_apply=bold_func,
            custom_style="font-weight: bold;"
        )
        self.bold_button.setText("B")
        self.tool_bar.addWidget(self.bold_button)

        # Italics button
        def ital_func(is_enabled, tmp_editor_ptr):
            if is_enabled:
                tmp_editor_ptr.setFontItalic(True)
            else:
                tmp_editor_ptr.setFontItalic(False)
        self.italic_button = CustomEditorButton(
            text_edit=self.text_edit,
            function_to_apply=ital_func,
            custom_style="font-style: italic;"
        )
        self.italic_button.setText("I")
        self.tool_bar.addWidget(self.italic_button)

        # Underline
        def util_func(is_enabled, tmp_editor_ptr):
            if is_enabled:
                tmp_editor_ptr.setFontUnderline(True)
            else:
                tmp_editor_ptr.setFontUnderline(False)
        self.under_button = CustomEditorButton(
            text_edit=self.text_edit,
            function_to_apply=util_func,
            custom_style="text-decoration: underline;"
        )
        self.under_button.setText("U")
        self.tool_bar.addWidget(self.under_button)
        # Order
        self.my_layout.addWidget(self.tool_bar)
        self.my_layout.addWidget(self.text_edit)
        self.setWidget(self.main_box)

    def check_button_states(self):
        self.bold_button.button_enabled = self.text_edit.fontWeight() >= QFont.Bold
        self.italic_button.button_enabled = self.text_edit.fontItalic()
        self.under_button.button_enabled = self.text_edit.fontUnderline()
        self.bold_button.style_button()
        self.italic_button.style_button()
        self.under_button.style_button()

    def closeEvent(self, event):
        for x in range(0 , len(self.my_parent.notes)):
            if self.my_parent.notes[x] == self:
                del self.my_parent.notes[x]
                self.deleteLater()
                super(QtW.QMdiSubWindow, self).closeEvent(event)
                return
        


    def to_notes_data(self) -> NotesData:
        return NotesData(
            notes_text=self.text_edit.toHtml(),
            x_pos=self.pos().x(),
            y_pos=self.pos().y()
        )

    def from_notes_data(self , data : NotesData): # -> NotesSubwindow
        self.text_edit.setHtml(data.notes_text)
        self.move(data.x_pos , data.y_pos)
