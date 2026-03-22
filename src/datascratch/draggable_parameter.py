import traceback
import PyQt5.QtWidgets as QtW
from decimal import Decimal
from datascratch.string_parameters_map import STRING_PARAMETER_MAP
from qfluentwidgets import LineEdit , SpinBox , CheckBox , ComboBox , DoubleSpinBox

def get_num_decimal_points(value : float) -> int:
    s = repr(Decimal(value))
    if '.' in s:
        return len(s.split('.')[1])
    else:
        return 0

# This is an abstract class BTW.
class Parameter(QtW.QWidget):
    """
    Abstract class to handle parameter fields.

    Args:
        QtW (_type_): _description_
    """
    def __init__(self):
        pass

    def text():
        pass

# QSpinBox for int's
# QDoubleSpinBox for doubles

class SingleLineParameter(LineEdit):
    def __init__(self , name , value,  **kwargs):
        super().__init__(**kwargs) 
        self.setText(str(value))

class IntSingleLine(SpinBox):
    def __init__(self , name , value,  **kwargs):
        super().__init__(**kwargs)
        max_value = 2147483647 # this is the 32-bit int max for signed ints
        self.setMinimum(-max_value) # Or use a very small number like -1e9
        self.setMaximum(max_value) 
        self.setValue(value)

    def text(self):
        return str(int(super().text()))

class FloatSingleLine(DoubleSpinBox):
    def __init__(self , name , value,  **kwargs):
        super().__init__(**kwargs)
        self.setMinimum(float('-inf')) # Or use a very small number like -1e9
        self.setMaximum(float('inf')) 
        #self.setDecimals(get_num_decimal_points(value))
        self.setValue(value)

    def text(self):
        return str(float(super().text()))

class BooleanSingleLine(CheckBox):
    def __init__(self , name , value,  **kwargs):
        super().__init__(**kwargs)
        self.setChecked(value)

    def text(self):
        return str(self.isChecked())
    
class StringListSingleLine(ComboBox):
    def __init__(self , name , value,  **kwargs):
        super().__init__(**kwargs)
        self.addItems(value)

    def text(self):
        return self.currentText()


    

BANNED_PARAMETERS = {
    # Some parameters don't need to be changed.
    # Example: Verbose, which prints stuff out to the console, can be hidden from the user.
    'n_jobs',
    'verbose',
    'warm_start',
    'dtype'
}


def parameter_filter(name : str , value , name_function : str) -> Parameter:
    """
    Args:
        name (str): _description_
        value (_type_): _description_

    Returns:
        Parameter: _description_
    """
    try:
        # Not a type
        if (name_function , name) in STRING_PARAMETER_MAP:
            curr_lst = STRING_PARAMETER_MAP[(name_function , name)]
            curr_list_gui = StringListSingleLine(name , curr_lst)
            curr_list_gui.setCurrentText(str(value))
            return curr_list_gui
        elif type(value) is int:
            return IntSingleLine(name , value)
        elif type(value) is float:
            return FloatSingleLine(name, value)
        elif type(value) is bool:
            return BooleanSingleLine(name , value)
        
        elif (type(value) is list) and (type(value[0]) is str):
            try:
                return StringListSingleLine(name , value)
            except Exception as e:
                print(str(e))
        else:
            return SingleLineParameter(name , value)
    except Exception as e:
        print(e)
        traceback.print_exception(e)
        return SingleLineParameter(name , value)