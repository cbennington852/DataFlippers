import pandas as pd
import sklearn
import src.datascratch.sklearn_engine as sklearn_engine
import pandas as pd
import sklearn
import seaborn as sns
from src.datascratch.sklearn_engine import Pipeline , EngineResults
import sklearn.model_selection as val

dataframe = pd.read_csv("resources/random_data.csv")

classifier_dataframe = pd.read_csv("resources/penguins.csv")

linear_pipe = sklearn.pipeline.Pipeline([
    ("Linear_m" , sklearn.linear_model.LinearRegression())
])

linear_pipe_2 = sklearn.pipeline.Pipeline([
    ("Linear_m" , sklearn.linear_model.Lasso())
])

tree_pipe_1 =  sklearn.pipeline.Pipeline([
    ("tree_m" , sklearn.tree.DecisionTreeRegressor(
        max_depth=100
    ))
])

classifier_pipe = sklearn.pipeline.Pipeline([
    ("Linear_m" , sklearn.linear_model.RidgeClassifier())
])

classifier_pipe_2 = sklearn.pipeline.Pipeline([
    ("tree" , sklearn.tree.DecisionTreeClassifier())
])


res : EngineResults = sklearn_engine.SklearnEngine.main_sklearn_pipe(
    main_dataframe=classifier_dataframe,
    pipeline_x_values=['island'],
    pipeline_y_value=['gender'],
    curr_pipelines=[
        
    ]
)
res.visual_plot.show()