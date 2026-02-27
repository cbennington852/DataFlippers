######################################################
# Loading the splash screen.
######################################################
import tkinter as tk
import importlib
splash_root = tk.Tk()
splash_root.title("Loading...")
splash_root.geometry("250x100")
label = tk.Label(splash_root, text="Loading...", font=("Helvetica", 12))
label.pack(pady=20)

######################################################
# Listing Dynamic Imports
######################################################
current_module_import_index = 0
FROM_IMPORT_TYPE = "from"
IMPORT_IMPORT_TYPE = "import"
list_modules = [
    # Type , selection , module type
   (IMPORT_IMPORT_TYPE , "sys" , "sys"),
   (IMPORT_IMPORT_TYPE , "sns" , "seaborn"),
   (IMPORT_IMPORT_TYPE , "os" , "os"),
   (IMPORT_IMPORT_TYPE , "pickle" , "pickle"),
   (IMPORT_IMPORT_TYPE , "traceback" , "traceback"),
   (IMPORT_IMPORT_TYPE , "time" , "time"),
   (IMPORT_IMPORT_TYPE , "QtW" ,"PyQt5.QtWidgets"),
   (IMPORT_IMPORT_TYPE , "qdarktheme" , "qdarktheme"),
   (IMPORT_IMPORT_TYPE , "pd" , "pandas"),
   (IMPORT_IMPORT_TYPE , "PipelineMother" , "datascratch.GUI_libary_and_pipeline_mother"),
   (FROM_IMPORT_TYPE , "GUILibary" , "datascratch.GUI_libary_and_pipeline_mother"),
   (FROM_IMPORT_TYPE , "PipelineMother" , "datascratch.GUI_libary_and_pipeline_mother"),
   (FROM_IMPORT_TYPE , "DataframeViewer" , "datascratch.dataframe_viewer"),
   (FROM_IMPORT_TYPE , "QIcon" , "PyQt5.QtGui"),
   (FROM_IMPORT_TYPE , "QPixmap" , "PyQt5.QtGui"),
   (FROM_IMPORT_TYPE , "SaveFileException" , "datascratch.save_file"),
   (FROM_IMPORT_TYPE , "SaveFile" , "datascratch.save_file"),
   (FROM_IMPORT_TYPE , "DataScratchSettings" , "datascratch.settings_manager"),
]

def dynamic_import_function(splash_root):
    """This function recursively and dynamically loads the libraries required for this application.
    """
    global current_module_import_index
    if current_module_import_index >= len(list_modules):
        splash_root.quit()
    else:
        type_module , selection , module = list_modules[current_module_import_index]
        if type_module == FROM_IMPORT_TYPE:
            import_from_module(module , selection)
        elif type_module == IMPORT_IMPORT_TYPE:
            import_import_module(selection , module)
        else:
            raise ValueError("Invalid import.")
        # Update current 
        label.config(text=f"Current {current_module_import_index} ... {selection}")
        current_module_import_index += 1

        # Recursive call
        splash_root.after(10, dynamic_import_function, splash_root)

def import_from_module(module_path , object_name):
    module = importlib.import_module(module_path)
    globals()[object_name] = getattr(module, object_name)

def import_import_module(alias  , module_name):
    module = importlib.import_module(module_name)
    globals()[alias] = module
    
# Recursive call
splash_root.after(10, dynamic_import_function, splash_root)
splash_root.mainloop()

# Cannot be dynamic cus of tkinter fighting PyQt
from datascratch.predictor_GUI import PredictionGUI
from datascratch.plotter import Plotter



