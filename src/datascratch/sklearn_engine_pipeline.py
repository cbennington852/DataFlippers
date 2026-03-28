import sklearn
from datascratch.list_of_acceptable_sklearn_functions import SklearnAcceptableFunctions



class Pipeline():

    def is_regressor(x):
        return x.__class__ in SklearnAcceptableFunctions.REGRESSORS
        

    def is_classifier(x):
        return x.__class__ in SklearnAcceptableFunctions.CLASSIFIERS

    REGRESSION = "regression"
    CLASSIFICATION = "classification"
    """
    A small class to hold a sklearn pipeline and optionally a validator.
    """
    def __init__(self , sklearn_pipeline : sklearn.pipeline.Pipeline , name = None , validator = None ):
        self.sklearn_pipeline = sklearn_pipeline
        self.validator = validator
        self.name = name
        self.model_results = None
        last_step_name , last_step_model = self.sklearn_pipeline.steps[-1]
        if self.name is None:
            self.name = last_step_model.__class__.__name__
        if Pipeline.is_classifier(last_step_model):
            self.supervised_learning_type = Pipeline.CLASSIFICATION
        elif Pipeline.is_regressor(last_step_model):
            self.supervised_learning_type = Pipeline.REGRESSION
        else:
            raise ValueError(f"Pipeline {name} has neither a regressor or classifier. Crashing")

    def predict(self , x_vals):
        return self.sklearn_pipeline.predict(x_vals)[0].item()
