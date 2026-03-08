# import tkinter as tk
# import importlib
# import multiprocessing
# from multiprocessing import current_process, Process
# from tkinter import ttk
# from PIL import Image, ImageTk
# from datascratch.logo_embbedded import get_datascratch_logo
# from datascratch.colors_and_appearance import AppAppearance
# import sys
# from enum import Enum


# ######################################################
# # Listing Dynamic Imports
# ######################################################
# current_module_import_index = 0
# FROM_IMPORT_TYPE = "from"
# IMPORT_IMPORT_TYPE = "import"
# list_modules = [
#     # Type , selection , module type
#    (IMPORT_IMPORT_TYPE , "QtW" ,"PyQt5.QtWidgets"),
#    (IMPORT_IMPORT_TYPE , "sys" , "sys"),
#    (IMPORT_IMPORT_TYPE , "sns" , "seaborn"),
#    (IMPORT_IMPORT_TYPE , "os" , "os"),
#    (IMPORT_IMPORT_TYPE , "pickle" , "pickle"),
#    (IMPORT_IMPORT_TYPE , "traceback" , "traceback"),
#    (IMPORT_IMPORT_TYPE , "time" , "time"),
#    (IMPORT_IMPORT_TYPE , "pd" , "pandas"),
#    (IMPORT_IMPORT_TYPE , "PipelineMother" , "datascratch.GUI_libary_and_pipeline_mother"),
#    (FROM_IMPORT_TYPE , "GUILibary" , "datascratch.GUI_libary_and_pipeline_mother"),
#    (FROM_IMPORT_TYPE , "PipelineMother" , "datascratch.GUI_libary_and_pipeline_mother"),
#    (FROM_IMPORT_TYPE , "DataframeViewer" , "datascratch.dataframe_viewer"),
#    (FROM_IMPORT_TYPE , "QIcon" , "PyQt5.QtGui"),
#    (FROM_IMPORT_TYPE , "QPixmap" , "PyQt5.QtGui"),
#    (FROM_IMPORT_TYPE , "SaveFileException" , "datascratch.save_file"),
#    (FROM_IMPORT_TYPE , "SaveFile" , "datascratch.save_file"),
#    (FROM_IMPORT_TYPE , "Qt" , "PyQt5.QtCore"),
#    (FROM_IMPORT_TYPE , "QFile" , "PyQt5.QtCore"),
#    (FROM_IMPORT_TYPE , "QIODevice" , "PyQt5.QtCore"),
#    (IMPORT_IMPORT_TYPE , "logging" , "logging"),
#    (FROM_IMPORT_TYPE , "QTextStream" , "PyQt5.QtCore"),
#    (FROM_IMPORT_TYPE , "DataScratchSettings" , "datascratch.settings_manager"),
# ]



# def center_window(win, width, height):
#     """Centers a Tkinter window on the screen."""
#     win.update_idletasks()
#     screen_width = win.winfo_screenwidth()
#     screen_height = win.winfo_screenheight()
#     x = (screen_width // 2) - (width // 2)
#     y = (screen_height // 2) - (height // 2)
#     win.geometry(f'{width}x{height}+{x}+{y}')

# splash_root = tk.Tk()
# splash_root.withdraw()
# splash_root.overrideredirect(True)
# splash_root.title("Loading...")
# center_window(splash_root , 600 , 400)
# label = tk.Label(splash_root, wraplength=370 , text="", font=("Helvetica", 12))
# label_summary = tk.Label(splash_root, wraplength=370, text=f"Loading {AppAppearance.APP_NAME} core libraries, this may be slower the first time.", font=("Helvetica", 12))

# pixel_scale = 10
# progress_bar = ttk.Progressbar(
#     splash_root,
#     orient='horizontal',
#     length=len(list_modules) * pixel_scale,
#     mode='determinate'
# )
# image_loaded = get_datascratch_logo().resize((250, 100), Image.Resampling.LANCZOS)
# print(image_loaded)
# img_ds_logo = ImageTk.PhotoImage(image_loaded)
# label_with_splash_image = tk.Label(splash_root, image=img_ds_logo)

# label_with_splash_image.pack(pady=20)
# label_summary.pack(pady=20)
# label.pack(pady=20)
# progress_bar.pack(pady=20)
# process_name = current_process().name
# if process_name == "MainProcess":
#     splash_root.deiconify()
# else:
#     pass

# def dynamic_import_function(splash_root):
#     """This function recursively and dynamically loads the libraries required for this application.
#     """
#     global current_module_import_index
#     if current_module_import_index >= len(list_modules):
#         splash_root.quit()
#     else:
#         type_module , selection , module = list_modules[current_module_import_index]
#         label.config(text=f"Loading Libraries ... {module}")
#         progress_bar['value'] = current_module_import_index * pixel_scale
#         if type_module == FROM_IMPORT_TYPE:
#             import_from_module(module , selection)
#         elif type_module == IMPORT_IMPORT_TYPE:
#             import_import_module(selection , module)
#         else:
#             raise ValueError("Invalid import.")
#         # Update current 
#         current_module_import_index += 1

#         # Recursive call
#         splash_root.after(2, dynamic_import_function, splash_root)

# def import_from_module(module_path , object_name):
#     module = importlib.import_module(module_path)
#     globals()[object_name] = getattr(module, object_name)

# def import_import_module(alias  , module_name):
#     module = importlib.import_module(module_name)
#     globals()[alias] = module
    
# # Recursive call
# splash_root.after(10, dynamic_import_function, splash_root)
# splash_root.mainloop()
# splash_root.destroy()


# Cannot be dynamic cus of tkinter fighting PyQt
# Or
# Cus they have special requirement
from datascratch.settings_manager import DataScratchSettings
from datascratch.predictor_GUI import PredictionGUI
from datascratch.plotter import Plotter
import qdarktheme
import sys
from datascratch import image_resources
from datascratch.logo_embbedded import get_datascratch_logo
from datascratch.colors_and_appearance import AppAppearance
import PyQt5.QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QMessageBox, QWidget, QVBoxLayout, QAction
from datascratch.GUI_libary_and_pipeline_mother import PipelineMother , GUILibary
from datascratch.sklearn_libary import SubLibary 
from datascratch.dataframe_viewer import DataframeViewer
import seaborn as sns
from datascratch import image_resources
from PyQt5.QtGui import QIcon , QPixmap
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import multiprocessing
from datascratch.plotter import Plotter
from datascratch.save_file import SaveFileException , SaveFile
import os
import pickle
import traceback
import time
import qdarktheme
import pandas as pd
from datascratch.settings_manager import DataScratchSettings
from datascratch.predictor_GUI import PredictionGUI
import logging
from qfluentwidgets import StyleSheetBase, Theme, isDarkTheme, qconfig

from qfluentwidgets import FluentWindow, setTheme, Theme
from qfluentwidgets import PushButton
from datascratch.theme_combo_box import ThemeComboBox


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
    SettingCardGroup, ExpandSettingCard, CustomColorSettingCard , TabWidget
)

from qfluentwidgets import CommandBar, Action, FluentIcon as FIF


logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)

windows = []
FILE_EXTENSION = "dscr"
FILE_EXTENSION_NAME = f"{AppAppearance.APP_NAME} Project File"
FILE_OPEN_STRING = f"All Files (*.{FILE_EXTENSION} *.csv *.xls);; {FILE_EXTENSION_NAME} (*.{FILE_EXTENSION});; CSV Files (*.csv);; Excel Files (*.xls);;"
# DataScratchSettings.getSettings().setValue(DataScratchSettings.RECENT_FILES_KEY , [])


class MainMenu(QtW.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"{AppAppearance.APP_NAME} Main Menu")
        self.title_image = QtW.QLabel(
            pixmap=QPixmap(":images/DataFlippers.png")
        )
        self.setMaximumWidth(self.title_image.width())

        # Set up basic ptrs
        my_layout = QtW.QVBoxLayout()
        main_box = QtW.QWidget()
        main_box.setLayout(my_layout)

        curr_toolbar = CommandBar()
        curr_toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        import_dataset = Action(
            QIcon(":images/import_dataset.svg"), "Import dataset", self
        )
        import_dataset.triggered.connect(self.import_datasets_clicked)
        curr_toolbar.addAction(import_dataset)

        import_dataset = Action(
            QIcon(":images/file_open.png"), "Open dataset", self
        )
        import_dataset.triggered.connect(self.import_datasets_clicked)
        curr_toolbar.addAction(import_dataset)

        # Render example dataset list
        example_datasets = [
            "minecraft_biome_and_block_counts",
            "penguins",
            "diamonds_measurements",
            "flower_measurements",
            "pokemon_stats",
            "random_data",
            "tips",
        ]

        def open_on_dataset(dataset_name):
            file = QFile(
                f":/example_datasets/{example_datasets[dataset_name.row()]}.csv"
            )
            if file.open(QIODevice.ReadOnly):
                df = pd.read_csv(file)
                curr = MainMenu.open_main_window_on_dataset(df)
                curr.show()
                windows.append(curr)
                self.deleteLater()

        # Render all of the example datasets.
        list_widget = ListWidget()
        list_widget.addItems(example_datasets)
        list_widget.clicked.connect(open_on_dataset)

        settings = DataScratchSettings.getSettings()
        recent_files_opened = settings.value(
            DataScratchSettings.RECENT_FILES_KEY, [], type=list
        )
        print("Recent files opened", recent_files_opened)
        recent_list_widget = ListWidget()
        recent_list_widget.addItems(recent_files_opened)
        recent_list_widget.clicked.connect(
            lambda x: open_on_file_handle(recent_files_opened[x.row()])
        )

        recent_group_box = QtW.QWidget()
        recent_group_box.setLayout(QtW.QVBoxLayout())
        recent_group_box.setMinimumHeight(100)
        recent_group_box.layout().addWidget(recent_list_widget)

        group_box = QtW.QWidget()
        group_box.setLayout(QtW.QVBoxLayout())
        group_box.setMinimumHeight(100)
        group_box.layout().addWidget(list_widget)


        # second_box
        second_box = QtW.QWidget()
        second_box_lay = QtW.QVBoxLayout()
        second_box.setLayout(second_box_lay)
        second_box_lay.addWidget(curr_toolbar)

        # Hello Text.
        hello_text = QtW.QLabel(
            f"""Welcome to {AppAppearance.APP_NAME}! You can import datasets through the Open Dataset button. Supported file types include excel, csv, parquet, and {FILE_EXTENSION}"""
        )
        hello_text.setWordWrap(True)

        tab_widget = TabWidget(self)
        tab_widget.tabBar.setAddButtonVisible(False)
        tab_widget.setTabsClosable(False)
        tab_widget.addPage(group_box , "Example Datasets")
        tab_widget.addPage(recent_group_box , "Recent Datasets")

        my_layout.addWidget(self.title_image)
        my_layout.addWidget(second_box)
        my_layout.addWidget(tab_widget)

        self.setCentralWidget(main_box)

    def open_main_window_on_dataset(dataframe):
        my_window = MainWindow(dataframe)  # Create an instance of our custom window
        return my_window

    def import_datasets_clicked(self):
        fileName, _ = QtW.QFileDialog.getOpenFileName(
            self, "Open File", "", FILE_OPEN_STRING, options=QtW.QFileDialog.Options()
        )
        if fileName:
            print("File name: ", fileName)
            open_on_file_handle(fileName)
            self.deleteLater()
        else:
            print("No file selected")


class MainWindow(QtW.QMainWindow):

    BASE_WINDOW_WIDTH = 1200
    BASE_WINDOW_HEIGHT = 800

    def __init__(self, dataframe, file_path=None):
        super().__init__()
        if file_path is not None:
            self.setWindowTitle(f"{file_path}")
        else:
            self.setWindowTitle(f"{AppAppearance.APP_NAME}")
        self.file_path = file_path

        self.resize(MainWindow.BASE_WINDOW_WIDTH, MainWindow.BASE_WINDOW_HEIGHT)

        # start a parsel.
        # load dataframe
        self.dataframe = dataframe

        self.libary = GUILibary(self.dataframe)
        self.dataframeViewer = DataframeViewer(self.dataframe)

        self.pipeline_mother = PipelineMother(self.dataframe)

        self.plotter = Plotter(self.pipeline_mother, self.dataframe)

        self.render_menu_bar()

        dock_libary = QtW.QDockWidget("", self)
        dock_dataframe = QtW.QDockWidget("", self)
        dock_plot = QtW.QDockWidget("", self)

        dock_libary.setTitleBarWidget(QtW.QWidget())
        dock_dataframe.setTitleBarWidget(QtW.QWidget())
        dock_plot.setTitleBarWidget(QtW.QWidget())


        dock_libary.setFeatures(
            dock_libary.features() & ~QtW.QDockWidget.DockWidgetClosable 
        )
        dock_dataframe.setFeatures(
            dock_dataframe.features() & ~QtW.QDockWidget.DockWidgetClosable 
        )
        dock_plot.setFeatures(
            dock_plot.features() & ~QtW.QDockWidget.DockWidgetClosable
        )

        dock_libary.setWidget(self.libary)
        dock_dataframe.setWidget(self.dataframeViewer)
        dock_plot.setWidget(self.plotter)

        self.addDockWidget(Qt.RightDockWidgetArea, dock_dataframe)
        self.addDockWidget(Qt.RightDockWidgetArea, dock_plot)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_libary)

        right_size = 20
        self.resizeDocks(
            [dock_plot, dock_dataframe], [right_size, right_size], Qt.Horizontal
        )

        self.setCentralWidget(self.pipeline_mother)

    def save_function(self, file_name=f"my_project.{FILE_EXTENSION}", no_popup=False):
        print(f"Dataframe {self.dataframe}")
        print(f"file_name : {file_name}")
        if not no_popup:
            file_path, _ = QtW.QFileDialog.getSaveFileName(
                None,
                "Save Project",
                file_name,
                f"{FILE_EXTENSION_NAME} (*.{FILE_EXTENSION});;All Files (*)",
            )
            if not file_path.endswith(f".{FILE_EXTENSION}"):
                file_path += f".{FILE_EXTENSION}"
        else:
            file_path = file_name
        if file_path:
            try:
                # Prepare the data object
                save_file = SaveFile(
                    pipelines_data=self.pipeline_mother.get_data(),
                    dataframe=self.dataframe,
                    columns_data=self.pipeline_mother.get_columns_data(),
                    list_notes_data=self.pipeline_mother.get_notes_data(),
                )

                # 2. Single 'wb' open.
                # This TRUNCATES the file automatically (replaces existing content).
                with open(file_path, "wb") as f:
                    pickle.dump(save_file, f)

                self.file_path = file_path

                self.setWindowTitle(self.file_path)

                print(f"Saved successfully to: {file_path}")
                # Also add this to the recently saved section.
                settings = DataScratchSettings.getSettings()
                curr_recently_opened = settings.value(
                    DataScratchSettings.RECENT_FILES_KEY, [], type=list
                )
                curr_recently_opened.append(file_path)
                curr_recently_opened = list(set(curr_recently_opened))
                settings.setValue(
                    DataScratchSettings.RECENT_FILES_KEY, curr_recently_opened
                )
            except OSError as e:
                QtW.QMessageBox.critical(None, "File Error", f"Could not open file: {e}")
            except Exception as e:
                traceback.print_exc()

    def open_on_saved_file(file_name=f"data_2.{FILE_EXTENSION}"):
        # basically open the file and then pass in all of the info for the things.
        with open(file_name, "rb") as file:
            loaded_data = pickle.load(file)
            if not isinstance(loaded_data, SaveFile):
                raise SaveFileException("File did not unpickle as a save file type.")

            # 1. Retrieve the dataframe
            df = loaded_data.dataframe
            if not isinstance(df, pd.DataFrame):
                raise SaveFileException("Pandas Dataframe could not be loaded.")
            # 2. Startup a new instance of a main window
            main_window = MainWindow(df, file_name)
            # 3. load the pipeline data into that main_window
            main_window.pipeline_mother.load_from_data(
                loaded_data.pipelines_data,
                loaded_data.columns_data,
                loaded_data.list_notes_data,
            )
            # 4. display the data.
            print(main_window)
            print("X cols", main_window.pipeline_mother.x_columns.get_cols())
            return main_window

    def render_menu_bar(self):
        menu = QtW.QToolBar()
        menu.setMovable(False)
        self.addToolBar(menu)
        
        # The File Menu
        file_tool_button = QtW.QToolButton()
        file_tool_button.setText("File")
        file_menu = QtW.QMenu("File")
        file_tool_button.setPopupMode(QtW.QToolButton.InstantPopup)
        file_tool_button.setMenu(file_menu)
        save_action = QtW.QAction("Save Project", self)
        save_action.triggered.connect(lambda x: self.save_button_pressed())
        file_menu.addAction(save_action)
        save_as_action = QtW.QAction("Save Project As", self)
        save_as_action.triggered.connect(lambda x: self.save_button_pressed())
        file_menu.addAction(save_as_action)
        open_action = QtW.QAction("Open Project", self)
        open_action.triggered.connect(self.open_button_pressed)
        file_menu.addAction(open_action)

        # Themes
        theme_tool_button = QtW.QToolButton()
        theme_tool_button.setText("Theme")
        theme_menu = QtW.QMenu("Theme")
        theme_tool_button.setPopupMode(QtW.QToolButton.InstantPopup)
        theme_tool_button.setMenu(theme_menu)
        themes_button  = ThemeComboBox()
        theme_action = QtW.QWidgetAction(self)
        theme_action.setDefaultWidget(themes_button)
        theme_menu.addAction(theme_action)



        menu.addWidget(file_tool_button)
        menu.addWidget(theme_tool_button)


    def save_button_pressed(self):
        if self.file_path is not None:
            try:
                self.save_function(file_name=self.file_path, no_popup=True)
            except:
                self.save_as_button_pressed()
        else:
            self.save_as_button_pressed()

    def save_as_button_pressed(self):
        self.save_function()

    def open_button_pressed(self):
        file_path, _ = QtW.QFileDialog.getOpenFileName(
            None, "Open Project", None, FILE_OPEN_STRING
        )
        if file_path:
            open_on_file_handle(file_path)


def filter_command_line_argument_return_dataframe(file_path) -> pd.DataFrame:
    # NOTE: We can later expand this to work on HTML tables and later SQL databases.
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".parquet"):
        return pd.read_parquet(file_path)
    excel_endings = [".xls", ".xlsx", ".xlsm", ".xlsb", ".odf", ".odt"]
    for ending in excel_endings:
        if file_path.endswith(ending):
            return pd.read_excel(file_path)
    # Else implied
    raise ValueError("Does not end in a valid file extension format")


def open_on_file_handle(file_handle):
    print("Attempted open on file handle", file_handle)
    if os.path.exists(file_handle):
        # parse command line argument
        if file_handle.endswith(f".{FILE_EXTENSION}"):
            try:
                # Make a splash
                main_window = MainWindow.open_on_saved_file(file_handle)
                main_window.show()
                windows.append(main_window)
            except Exception as e:
                traceback.print_exc()
                QtW.QMessageBox.critical(
                    None,  # Parent: Use None if not within a QWidget class
                    "Error opening Save file",  # Title bar text
                    f"{str(e)}",  # Main message
                )
        # This is exported / saved models / pipelines
        elif file_handle.endswith(PredictionGUI.model_save_extension):
            try:
                with open(file_handle, "rb") as file:
                    loaded_data = pickle.load(file)
                    print("Opened and loaded pickle")
                    model_pred = PredictionGUI(loaded_data, True)
                    new_win = QtW.QMainWindow()
                    new_win.setWindowTitle(f"{AppAppearance.APP_NAME} Pipeline File")
                    new_win.setCentralWidget(model_pred)
                    new_win.show()
                    windows.append(new_win)
                    print("new_win", new_win)
            except Exception as e:
                traceback.print_exc()
                QtW.QMessageBox.critical(
                    None,  # Parent: Use None if not within a QWidget class
                    "Error opening saved model file",  # Title bar text
                    f"{str(e)}",  # Main message
                )
        else:
            try:
                df = filter_command_line_argument_return_dataframe(file_handle)
                try:
                    main_window = MainMenu.open_main_window_on_dataset(df)
                    main_window.show()
                    windows.append(main_window)
                except Exception as e:
                    QtW.QMessageBox.critical(
                        None,  # Parent: Use None if not within a QWidget class
                        "Internal Error opening file",  # Title bar text
                        f"{str(e)}",  # Main message
                    )
            except Exception as e:
                QtW.QMessageBox.critical(
                    None,  # Parent: Use None if not within a QWidget class
                    "File type not supported",  # Title bar text
                    f"{str(e)}",  # Main message
                )
    else:
        QtW.QMessageBox.critical(
            None,  # Parent: Use None if not within a QWidget class
            "Error opening file. File does not exist.",  # Title bar text
            f"File {file_handle} was not found.",  # Main message
        )

from qfluentwidgets import FluentWindow, setTheme, Theme


def main():
    #QtW.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    #QtW.QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QtW.QApplication(sys.argv)  # Create the application instance
    setTheme(Theme.LIGHT)
    # file_curr = QFile(f":/styles/new_stylesheet.css")
    # if not file_curr.open(
    #     QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text
    # ):
    #     print(f"Error: Could not open file stylesheet- {file_curr.errorString()}")
    #     return None
    # stream = QTextStream(file_curr)
    # new_style = stream.readAll()
    # app.setStyleSheet(new_style)

    if len(sys.argv) > 1:
        open_on_file_handle(sys.argv[1])
    else:
        main_menu = MainMenu()
        main_menu.show()

    app.setWindowIcon(QIcon(":/images/DataPenguins.svg"))
    


    sys.exit(app.exec_())  # Start the application's event loop


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
