
class SklearnEngineJobRequest():
    def __init__(self , dataframe , pipelines , x_cols , y_cols , curr_theme):
        self.dataframe = dataframe
        self.lst_engine_pipelines = pipelines
        self.x_cols = x_cols
        self.y_cols = y_cols
        self.curr_theme = curr_theme