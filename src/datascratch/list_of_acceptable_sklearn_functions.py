import sklearn
import sklearn.linear_model as lin
import sklearn.ensemble as ens
import sklearn.preprocessing as pre
import sklearn.model_selection as val
import sklearn.neural_network as neu
import sklearn.tree as tre
import sklearn.svm as svm
import sklearn.cluster as cls
import sklearn.neighbors as nei
import sklearn.dummy as dum


class SklearnAcceptableFunctions:

    ##############################################################
    # REGRESSORS
    ##############################################################

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
        dum.DummyRegressor,
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
    REGRESSORS_NEIGHBORS = [nei.KNeighborsRegressor , nei.RadiusNeighborsRegressor] 

    REGRESSORS = (
        REGRESSORS_ENSEMBLE
        + REGRESSORS_LINEAR
        + REGRESSORS_NEURAL_NETWORK
        + REGRESSORS_TREE
        + REGRESSORS_SUPPORT_VECTOR_MACHINES
        + REGRESSORS_NEIGHBORS
    )

    ##############################################################
    # CLASSIFIERS
    ##############################################################
    CLASSIFIERS_LINEAR = [
        lin.LogisticRegression,
        lin.RidgeClassifier,
        lin.PassiveAggressiveClassifier,
        lin.Perceptron,
        lin.SGDClassifier,
        dum.DummyClassifier,

    ]
    CLASSIFIERS_SUPPORT_VECTOR_MACHINES = [
        svm.LinearSVC,
        svm.NuSVC,
        svm.SVC
    ]
    CLASSIFIERS_ENSEMBLE = [
        ens.AdaBoostClassifier,
        ens.BaggingClassifier,
        ens.ExtraTreesClassifier,
        ens.GradientBoostingClassifier,
        ens.HistGradientBoostingClassifier,
        ens.RandomForestClassifier,
    ]
    CLASSIFIERS_CLUSTERING = [

    ]
    CLASSIFIERS_NEIGHBORS = [nei.KNeighborsClassifier , nei.RadiusNeighborsClassifier] 

    CLASSIFIERS_NEURAL = [neu.MLPClassifier]

    CLASSIFIERS_TREE = [tre.DecisionTreeClassifier, tre.ExtraTreeClassifier]

    CLASSIFIERS = (
        CLASSIFIERS_ENSEMBLE
        + CLASSIFIERS_LINEAR
        + CLASSIFIERS_NEURAL
        + CLASSIFIERS_TREE
        + CLASSIFIERS_SUPPORT_VECTOR_MACHINES
        + CLASSIFIERS_NEIGHBORS
        + CLASSIFIERS_CLUSTERING
    )

    ##############################################################
    # PRE_PROCESSORS
    ##############################################################
    # Needs a 'fit' and 'transform'


    PREPROCESSORS_CLUSTER = [
        cls.KMeans,
        cls.Birch,
        cls.BisectingKMeans,
    ]

    PREPROCESSORS_SCALAR = [
        pre.MaxAbsScaler,
        pre.MinMaxScaler,
        pre.RobustScaler,
        pre.StandardScaler,
        pre.Normalizer,
        pre.PowerTransformer,
        pre.QuantileTransformer,
    ]

    PREPROCESSORS_TRANSFORMER = [
        pre.PolynomialFeatures,
        pre.SplineTransformer,
    ]
    
    PREPROCESSORS = PREPROCESSORS_TRANSFORMER + PREPROCESSORS_CLUSTER + PREPROCESSORS_SCALAR



    ##############################################################
    # VALIDATORS
    ##############################################################

    VALIDATORS = [
        val.KFold,
        val.StratifiedKFold,
        val.LeaveOneOut,
    ]

    MODELS = CLASSIFIERS + REGRESSORS
