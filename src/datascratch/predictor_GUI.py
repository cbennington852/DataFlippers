from PyQt5.QtWidgets import QWidget , QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QMessageBox, QWidget, QVBoxLayout, QLabel
import PyQt5.QtWidgets as QtW
from PyQt5.QtCore import  QPoint
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag , QIcon
import PyQt5.QtCore as QtCore 
import ast
import pandas as pd
import pickle
from datascratch.draggable_parameter import parameter_filter
import traceback
from datascratch.sklearn_engine import EngineResults , Pipeline

FILE_EXTENSION = 'dscr'
FILE_EXTENSION_NAME = 'Data Scratch Project File'
FILE_OPEN_STRING = f"All Files (*.{FILE_EXTENSION} *.csv *.xls);; {FILE_EXTENSION_NAME} (*.{FILE_EXTENSION});; CSV Files (*.csv);; Excel Files (*.xls);;"


class RowPredictor(QtW.QTabWidget):
    def __init__(self, engine_results,  **kwargs):
        super().__init__( **kwargs)
        
        self.engine_results = engine_results

        self.addTab(self.upload_input_dataset() , "Upload dataset")
        self.addTab(QWidget() , "View Dataset")
        self.addTab(QWidget() , "Run Predictions")

        # Allow for upload of .csv .exel .parquet

    def show_uploaded_dataset(self) -> QWidget:
        pass
    
    def upload_input_dataset(self) -> QWidget:
        main = QWidget()
        my_layout = QtW.QVBoxLayout()
        main.setLayout(my_layout)

        def input_dataset_clicked():
            filename, _ = QtW.QFileDialog.getOpenFileName(
                self,
                "Select a dataset to import for prediction",
                "", # Start directory (empty string defaults to current working directory)
                FILE_OPEN_STRING # File filters
            )
            if filename:
                pass
            else:
                pass

        input_dataset = QtW.QPushButton("Import dataset for prediction!")
        input_dataset.clicked.connect(input_dataset_clicked)
        return main


class SinglePredictor(QtW.QGroupBox):
    def __init__(self, title, engine_results,  **kwargs):
        super().__init__(title , **kwargs)
        self.my_layout = QtW.QHBoxLayout()
        self.setLayout(self.my_layout)
        self.engine_results = engine_results

         # 1. Remove all of the widgets from this page
        for child in self.findChildren(QtW.QWidget):
            child.deleteLater()

        # 2. Add Text entry for each of the x_cols
        x_cols_box = QtW.QGroupBox("Inputs")
        x_cols_box_layout = QtW.QFormLayout()
        x_cols_box.setLayout(x_cols_box_layout)
        self.x_cols_ptr_lst = []
        for x_col in self.engine_results.x_cols:
            # We could also use the parameter class here.
            x_col_name = QtW.QLabel(x_col)
            x_col_entry = None
            if self.engine_results.is_column_in_list_converted_columns(x_col):
                converted_col = self.engine_results.get_converted_column(x_col)
                x_col_entry = parameter_filter(x_col , converted_col.code_map)
            else:
                x_col_entry = parameter_filter(x_col , self.engine_results.column_types[x_col])
                # This is a string! 
                
            self.x_cols_ptr_lst.append(x_col_entry)
            x_cols_box_layout.addRow(x_col_name , x_col_entry)

        # 3. Add Boxes, with each model being a prediction "box"
        pipeline_holder = QtW.QGroupBox("Pipelines")
        pipeline_holder_layout = QtW.QVBoxLayout()
        pipeline_holder.setLayout(pipeline_holder_layout)
        self.pipelines_groupbox_ptr = []
        for pipeline in self.engine_results.trained_models:
            curr_pipeline = PredictionGUIPipeline(pipeline)
            self.pipelines_groupbox_ptr.append(curr_pipeline)
            pipeline_holder_layout.addWidget(curr_pipeline)

        self.my_layout.addWidget(x_cols_box)
        self.my_layout.addWidget(pipeline_holder)

        # 4. Add and connect a button to get each prediction.
            # NOTE : the backend for this will be handled by the 
        # 4. We could also try having it be on type.

        self.predict_button = QPushButton("Predict")
        self.predict_button.clicked.connect(self.run_all_predictions)
        self.my_layout.addWidget(self.predict_button)

    def run_all_predictions(self):
        # Get all of the x_values
        try:
            x_values = []
            for x_col in self.x_cols_ptr_lst:
                curr_value = x_col.text()
                x_values.append(ast.literal_eval(curr_value))

            res = self.engine_results.predict(x_values)
            for pipeline_ptr , value in res.items():
                for gui_pipe in self.pipelines_groupbox_ptr:
                    if pipeline_ptr == gui_pipe.pipeline:
                        gui_pipe.pred_value.setText(str(value))
            print(res)
        except Exception as e:
            QtW.QMessageBox.critical(
                 None,                        # Parent: Use None if not within a QWidget class
                 "Engine Prediction Error",            # Title bar text
                 f"{str(e)}" # Main message
            )
            traceback.print_exception(e)
            print(e)


class PredictionGUI(QtW.QScrollArea):
    def __init__(self, engine_results : EngineResults,  hide_export_features = False,  **kwargs):
        """
        A small part of the GUI which allows users to predict 

        Args:
            engine_results (EngineResults): _description_
            hide_export_features (bool, optional): _description_. Defaults to False.
        """
        super().__init__(**kwargs)

        self.engine_results = engine_results
        # Setup layout
        self.main = QtW.QWidget()
        self.my_layout = QtW.QHBoxLayout()
        self.main.setLayout(self.my_layout)
        self.left = SinglePredictor("Predict Single Value" , self.engine_results)
        self.my_layout.addWidget(self.left)
        self.my_layout.addWidget(RowPredictor(self.engine_results))
        self.setWidget(self.main)

        # GENERAL PLAN:
            # Have a GroupBox for the x_cols
            # Have an individual groupbox for each predictor.

       
        # self.export_as_software_button = QtW.QToolButton(self.main)
        # self.export_as_software_button.setIcon(QIcon(":images/export_icon.svg"))
        # self.export_as_software_button.setText("& Export")
        # self.export_as_software_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        # self.export_as_software_button.setPopupMode(QtW.QToolButton.InstantPopup)
        # self.export_as_software_button.setMenu(QtW.QMenu(self.export_as_software_button))


        # export_as_software_action = QtW.QAction("Export as software" , self.main)
        # export_as_software_action.triggered.connect(lambda x : self.export_function_button_clicked(self.export_as_software , f"DataScratch Pipeline File (*{PredictionGUI.model_save_extension});;"))
        # self.export_as_software_button.menu().addAction(export_as_software_action)

        # export_as_pickle_action = QtW.QAction("Export as python pickle" , self.main)
        # export_as_pickle_action.triggered.connect(lambda x : self.export_function_button_clicked(self.export_as_pickle , "Pickle  (*.pickle);;"))
        # self.export_as_software_button.menu().addAction(export_as_pickle_action)


        # Assemble page

        # if hide_export_features == False:
        #     self.my_layout.addWidget(self.export_as_software_button)
        # self.setWidget(self.main)

        # Adding the single point predictor. 
        


    # def export_as_pickle(self):
    #     if not file_name.endswith('.pickle'):
    #         file_name += '.pickle'

    #     with open(file_name, 'wb') as f:
    #         pickle.dump(self.engine_results, f)



    # def export_function_button_clicked(self , function , file_type_string):
        
    #     # 1. Open a file dialog
    #     file_path, _ = QtW.QFileDialog.getSaveFileName(
    #             None, "Save Project", "",file_type_string 
    #         )
    #     if not file_path:
    #         return
    #     try:
    #         function(file_path)
    #     except Exception as e:
    #         QtW.QMessageBox.critical(
    #                     None,                        # Parent: Use None if not within a QWidget class
    #                     "Error Saving file",            # Title bar text
    #                     f"{str(e)}" # Main message
    #                 )

        

    # def export_as_software(self , file_name : str):
    #     # 2. Save the Engine Results as a pickled file with special file extension.
    #     if not file_name.endswith(PredictionGUI.model_save_extension):
    #         file_name += PredictionGUI.model_save_extension

    #     with open(file_name, 'wb') as f:
    #         pickle.dump(self.engine_results, f)

    



class PredictionGUIPipeline(QtW.QGroupBox):
    def __init__(self, pipeline : Pipeline, **kwargs):
        super().__init__(pipeline.name , **kwargs)
        self.pipeline = pipeline
        self.my_layout = QtW.QVBoxLayout()
        self.setLayout(self.my_layout)
        self.pred_value = QtW.QLabel("")
        self.my_layout.addWidget(self.pred_value)
