from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QMainWindow,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QMessageBox,
    QWidget,
    QVBoxLayout,
    QLabel,
)
from datascratch.colors_and_appearance import AppAppearance
import PyQt5.QtWidgets as QtW
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QIcon
import PyQt5.QtCore as QtCore
import ast
from PyQt5.QtCore import Qt, QSize
import pandas as pd
import pickle
from datascratch.dataframe_viewer import DataframeViewer
from datascratch.draggable_parameter import parameter_filter
import traceback
from datascratch.sklearn_engine import EngineResults, Pipeline
from qfluentwidgets import ScrollArea , PushButton

FILE_EXTENSION = "dscr"
FILE_EXTENSION_NAME = "Data Scratch Project File"
FILE_OPEN_STRING = f"All Files (*.{FILE_EXTENSION} *.csv *.xls);; {FILE_EXTENSION_NAME} (*.{FILE_EXTENSION});; CSV Files (*.csv);; Excel Files (*.xls);;"


class RowPredictor(QWidget):
    def __init__(self, engine_results, **kwargs):
        super().__init__(**kwargs)
        self.engine_results: EngineResults = engine_results
        self.my_layout = QtW.QHBoxLayout()
        self.setLayout(self.my_layout)

        # Note: This is the pointer to the current input dataframe
        self.new_df_viewer: DataframeViewer = None

        # We gonna seperatre this into two sections.
        # Left
        # StackedWidget
        # Upload dataset, which shifts to view dataset, with a back button on upload.
        # Run Predications on dataframe, which has a run predications button, and a DataframeViewer. This deletes previous dataframes on run preds.

        # Left side setup
        self.left = QWidget()
        self.left_lay = QtW.QStackedLayout()
        self.left.setLayout(self.left_lay)
        # Stack 0 ... upload_input_dataset
        self.left_lay.addWidget(self.upload_input_dataset())
        # Stack 1 ... view dataset
        self.left_lay.addWidget(self.view_dataset())

        self.right = QWidget()
        self.right_lay = QtW.QVBoxLayout()
        self.right.setLayout(self.right_lay)
        self.right_lay.addWidget(self.run_predictions_widget())

        self.my_layout.addWidget(self.left)
        self.my_layout.addWidget(self.right)

    def remove_previous_dataset(self):
        try:
            self.new_dataframe_results_viewer
            self.new_dataframe_results_viewer.deleteLater()
            del self.new_dataframe_results_viewer
        except Exception as e:
            pass

    def view_dataset(self) -> QWidget:
        self.view_widget = QtW.QGroupBox("Imported Dataset")
        self.view_layout = QtW.QVBoxLayout()
        self.view_widget.setLayout(self.view_layout)
        return self.view_widget

    def run_predictions_on_dataframe(self) -> pd.DataFrame:
        self.remove_previous_dataset()
        curr_dataframe = None
        try:
            curr_dataframe = self.new_df_viewer.get_pd_dataframe()
        except Exception as e:
            QtW.QMessageBox.warning(
                None,  # Parent: Use None if not within a QWidget class
                f"No dataframe uploaded",  # Title bar text
                f"Please upload a dataframe to run predictions on. Supported types include (.csv , .xlsx)",  # Main message
            )
        # Drop na values
        curr_dataframe = curr_dataframe.dropna()
        results_prediction_df = None
        try:
            results_prediction_df = self.engine_results.predict_from_df(curr_dataframe)
            self.new_dataframe_results_viewer = DataframeViewer(results_prediction_df)
            self.pred_layout.addWidget(self.new_dataframe_results_viewer)
        except Exception as e:
            QtW.QMessageBox.critical(
                None,  # Parent: Use None if not within a QWidget class
                f"Prediction Error",  # Title bar text
                f"{str(e)}",  # Main message
            )

    def run_predictions_widget(self) -> QWidget:
        self.pred_widget = QWidget()
        self.pred_layout = QtW.QVBoxLayout()
        self.pred_widget.setLayout(self.pred_layout)

        # Run predicitons button
        self.run_prediction_button = QPushButton("Run All Pipeline Predictions")
        play_icon = self.style().standardIcon(QtW.QStyle.SP_MediaPlay)
        self.run_prediction_button.setIcon(play_icon)
        self.pred_layout.addWidget(self.run_prediction_button)
        self.run_prediction_button.clicked.connect(self.run_predictions_on_dataframe)
        self.pred_widget.setVisible(False)
        return self.pred_widget

    def upload_input_dataset(self) -> QWidget:
        main = QWidget()
        my_layout = QtW.QVBoxLayout()
        main.setLayout(my_layout)

        def input_dataset_clicked():
            filename, _ = QtW.QFileDialog.getOpenFileName(
                self,
                "Select a dataset to import for prediction",
                "",  # Start directory (empty string defaults to current working directory)
                FILE_OPEN_STRING,  # File filters
            )
            if filename:
                new_df = None
                if filename.endswith(".csv"):
                    new_df = pd.read_csv(filename)
                elif filename.endswith(".xlsx"):
                    new_df = pd.read_excel(filename)
                else:
                    QtW.QMessageBox.warning(
                        None,  # Parent: Use None if not within a QWidget class
                        f"Unsupported file type",  # Title bar text
                        f"File {filename} type not supported. supported types include (.csv , .xlsx)",  # Main message
                    )
                # Now we have th excel
                for child in self.view_widget.findChildren(QtW.QWidget):
                    child.deleteLater()

                self.back_button = PushButton("< Back")

                def back_function():
                    self.new_df_viewer = None
                    self.left_lay.setCurrentIndex(0)
                    # Remove previous dataset.
                    self.remove_previous_dataset()

                    self.pred_widget.setVisible(False)

                self.back_button.clicked.connect(back_function)
                self.view_layout.addWidget(self.back_button)

                group_wrapper = QtW.QGroupBox()
                wrapper_layout = QtW.QVBoxLayout()
                group_wrapper.setLayout(wrapper_layout)
                self.new_df_viewer = DataframeViewer(new_df)
                wrapper_layout.addWidget(self.new_df_viewer)
                self.left_lay.setCurrentIndex(1)
                self.pred_widget.setVisible(True)
                self.view_layout.addWidget(group_wrapper)
            else:
                pass

        input_dataset = PushButton()
        label_with_info = QLabel(
            f"Upload a dataset for the model to perform predictions on. Supported formats include .csv and .xlsx. Additional Documentation available on our website at {AppAppearance.WEBSITE_URL}/Basics/Predictions"
        )
        label_with_info.setWordWrap(True)
        input_dataset.setText("Import dataset for prediction!")
        input_dataset.setIcon(QIcon(":images/import_dataset.svg"))
        input_dataset.setIconSize(QSize(48, 48))
        input_dataset.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        input_dataset.clicked.connect(input_dataset_clicked)
        my_layout.addWidget(label_with_info)
        my_layout.addWidget(input_dataset)
        return main


class SinglePredictor(QtW.QWidget):
    def __init__(self, title, engine_results, **kwargs):
        super().__init__(**kwargs)
        self.my_layout = QtW.QVBoxLayout()
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
                x_col_entry = parameter_filter(x_col, converted_col.code_map)
            else:
                x_col_entry = parameter_filter(
                    x_col, self.engine_results.column_types[x_col]
                )
                # This is a string!

            self.x_cols_ptr_lst.append(x_col_entry)
            x_cols_box_layout.addRow(x_col_name, x_col_entry)

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
                print("Current Value : " , curr_value)
                new_val = None
                try:
                    new_val = ast.literal_eval(curr_value)
                except:
                    new_val = str(curr_value)
                x_values.append(new_val)

            res = self.engine_results.predict(x_values)
            for pipeline_ptr, value in res.items():
                for gui_pipe in self.pipelines_groupbox_ptr:
                    if pipeline_ptr == gui_pipe.pipeline:
                        gui_pipe.pred_value.setText(str(value))
            print(res)
        except Exception as e:
            QtW.QMessageBox.critical(
                None,  # Parent: Use None if not within a QWidget class
                "Engine Prediction Error",  # Title bar text
                f"{str(e)}",  # Main message
            )
            traceback.print_exception(e)
            print(e)


class PredictionGUI(QtW.QTabWidget):
    def __init__(
        self, engine_results: EngineResults, hide_export_features=False, **kwargs
    ):
        """
        A small part of the GUI which allows users to predict

        Args:
            engine_results (EngineResults): _description_
            hide_export_features (bool, optional): _description_. Defaults to False.
        """
        super().__init__(**kwargs)

        self.engine_results = engine_results
        # Setup layout
        self.setSizePolicy(
            QtW.QSizePolicy.Policy.Expanding, QtW.QSizePolicy.Policy.Preferred
        )
        self.left = SinglePredictor("Predict Single Value", self.engine_results)
        self.right = RowPredictor(self.engine_results)
        self.addTab(self.right, "Predict Multiple Values")
        self.addTab(self.left, "Predict Single Value")

        # GENERAL PLAN:
        # Have a GroupBox for the x_cols
        # Have an individual groupbox for each predictor.


class PredictionGUIPipeline(QtW.QGroupBox):
    def __init__(self, pipeline: Pipeline, **kwargs):
        super().__init__(pipeline.name, **kwargs)
        self.pipeline = pipeline
        self.my_layout = QtW.QVBoxLayout()
        self.setLayout(self.my_layout)
        self.pred_value = QtW.QLabel("")
        self.my_layout.addWidget(self.pred_value)
