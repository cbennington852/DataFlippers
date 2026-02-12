from datascratch.GUI_libary_and_pipeline_mother import PipelineData , ColumnsWindowData
import pandas as pd
from datascratch.notes_subwindow import NotesData

class SaveFile():
    """
    Python object to hold the save file information.
    """
    def __init__(self , pipelines_data : list[PipelineData] , dataframe : pd.DataFrame , columns_data : ColumnsWindowData , list_notes_data : list[NotesData]):
        # Check types.
        self.pipelines_data = pipelines_data
        self.dataframe = dataframe
        self.columns_data = columns_data
        self.list_notes_data = list_notes_data

class SaveFileException(Exception):
    def __init__(self, *args):
        super().__init__(*args)