import sklearn
import sklearn.linear_model as lin
import sklearn.ensemble as ens
import sklearn.preprocessing as pre
import sklearn.model_selection as val
import sklearn.neural_network as neu
import sklearn.tree as tre
import sklearn.svm as svm


class SklearnAcceptableFunctions:
    REGRESSORS_LINEAR = [
        lin.LinearRegression,
        lin.Ridge,
        lin.ARDRegression,
        lin.BayesianRidge,
        lin.ElasticNet,
        lin.GammaRegressor,
        lin.HuberRegressor,
        lin.Lars,
        lin.Lasso,
        lin.LassoLars,
        lin.LassoLarsIC,
        lin.PassiveAggressiveRegressor,
        lin.PoissonRegressor,
        lin.QuantileRegressor,
        lin.RANSACRegressor,
        lin.SGDRegressor,
        lin.TheilSenRegressor,
        lin.TweedieRegressor,
    ]
    REGRESSORS_SUPPORT_VECTOR_MACHINES = [
        svm.LinearSVR,
        svm.NuSVR,
        svm.SVR
    ]
    REGRESSORS_ENSEMBLE = [
        ens.AdaBoostRegressor,
        ens.BaggingRegressor,
        ens.ExtraTreesRegressor,
        ens.GradientBoostingRegressor,
        ens.HistGradientBoostingRegressor,
        ens.RandomForestRegressor,
    ]
    REGRESSORS_NEURAL_NETWORK = [neu.MLPRegressor]
    REGRESSORS_TREE = [tre.DecisionTreeRegressor, tre.ExtraTreeRegressor]

    REGRESSORS = (
        REGRESSORS_ENSEMBLE
        + REGRESSORS_LINEAR
        + REGRESSORS_NEURAL_NETWORK
        + REGRESSORS_TREE
        + REGRESSORS_SUPPORT_VECTOR_MACHINES
    )

    CLASSIFIERS_LINEAR = [
        lin.LogisticRegression,
        lin.RidgeClassifier,
        lin.PassiveAggressiveClassifier,
        lin.Perceptron,
        lin.SGDClassifier,
    ]
    CLASSIFIERS_SUPPORT_VECTOR_MACHINES = {
        svm.LinearSVC,
        svm.NuSVC,
        svm.SVC
    }
    CLASSIFIERS_ENSEMBLE = [
        ens.AdaBoostClassifier,
        ens.BaggingClassifier,
        ens.ExtraTreesClassifier,
        ens.GradientBoostingClassifier,
        ens.HistGradientBoostingClassifier,
        ens.RandomForestClassifier,
    ]

    CLASSIFIERS_NEURAL = [neu.MLPClassifier]

    CLASSIFIERS_TREE = [tre.DecisionTreeClassifier, tre.ExtraTreeClassifier]

    # | is union in set
    CLASSIFIERS = (
        CLASSIFIERS_ENSEMBLE
        + CLASSIFIERS_LINEAR
        + CLASSIFIERS_NEURAL
        + CLASSIFIERS_TREE
        + CLASSIFIERS_SUPPORT_VECTOR_MACHINES
    )

    PREPROCESSORS = [
        pre.MaxAbsScaler,
        pre.MinMaxScaler,
        pre.Normalizer,
        pre.PolynomialFeatures,
        pre.PowerTransformer,
        pre.QuantileTransformer,
        pre.RobustScaler,
        pre.SplineTransformer,
        pre.StandardScaler,
    ]

    VALIDATORS = [
        val.KFold,
        val.StratifiedKFold,
        val.LeaveOneOut,
    ]

    MODELS = CLASSIFIERS + REGRESSORS
