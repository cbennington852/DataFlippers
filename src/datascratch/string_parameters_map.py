STRING_PARAMETER_MAP = {
    ("Ridge", "solver"): (
        "auto",
        "svd",
        "cholesky",
        "lsqr",
        "sparse_cg",
        "sag",
        "saga",
        "lbfgs",
    ),
    ("ElasticNet", "selection"): ("cyclic", "random"),
    ("GammaRegressor", "solver"): ("lbfgs", "newton-cholesky"),
    ("Lars", "precompute"): ("auto", "True", "False"),
    ("Lasso", "selection"): ("cyclic", "random"),
    #
    ("LassoLars", "precompute"): ("auto", "True", "False"),
    ("LassoLarsIC", "criterion"): ("aic", "bic"),
    ("LassoLarsIC", "precompute"): ("auto", "True", "False"),
    ("PassiveAggressiveRegressor", "loss"): (
        "epsilon_insensitive",
        "squared_epsilon_insensitive",
    ),
    ("PoissonRegressor", "solver"): ("lbfgs", "newton-cholesky"),
    ("QuantileRegressor", "solver"): (
        "highs-ds",
        "highs-ipm",
        "highs",
        "osqp",
        "interior-point",
    ),
    #
    ("RANSACRegressor", "loss"): (
        "absolute_error", "squared_error"
    ),
    ("TweedieRegressor", "link"): (
        "auto", "identity", "log"
    ),
    ("TweedieRegressor", "solver"): (
        "lbfgs", "newton-cholesky"
    ),
    ("DummyRegressor", "strategy"): (
        "mean", "median", "quantile", "constant"
    ),
    ("AdaBoostRegressor", "loss"): (
        "linear", "square", "exponential"
    ),
    #
    ("ExtraTreesRegressor", "criterion"): (
        "squared_error", "absolute_error", "friedman_mse", "poisson"
    ),
    ("GradientBoostingRegressor", "loss"): (
        "squared_error", "absolute_error", "huber", "quantile"
    ),
    ("GradientBoostingRegressor", "criterion"): (
        "friedman_mse", "squared_error"
    ),
    ("HistGradientBoostingRegressor", "loss"): (
        "squared_error", "absolute_error", "gamma", "poisson", "quantile"
    ),
    ("HistGradientBoostingRegressor", "categorical_features"): (
        "from_dtype", "None", "warn"
    ),
    ("HistGradientBoostingRegressor", "early_stopping"): (
        "auto", "True", "False"
    ),
    ("HistGradientBoostingRegressor", "scoring"): (
        "loss", "None"
    ),
    ("RandomForestRegressor", "criterion"): (
        "squared_error", "absolute_error", "friedman_mse", "poisson"
    ),
    #
    ("MLPRegressor", "activation"): ("identity", "logistic", "tanh", "relu"),
    ("MLPRegressor", "solver"): ("lbfgs", "sgd", "adam"),
    # ("MLPRegressor", "batch_size"): ("auto", int), # 'auto' = min(200, n_samples)
    ("MLPRegressor", "learning_rate"): ("constant", "invscaling", "adaptive"),
    
    ("DecisionTreeRegressor", "criterion"): ("squared_error", "friedman_mse", "absolute_error", "poisson"),
    ("DecisionTreeRegressor", "splitter"): ("best", "random"),
    
    ("ExtraTreeRegressor", "criterion"): ("squared_error", "friedman_mse", "absolute_error", "poisson"),
    ("ExtraTreeRegressor", "splitter"): ("best", "random"),
    
    ("LinearSVR", "loss"): ("epsilon_insensitive", "squared_epsilon_insensitive"),
    ("LinearSVR", "dual"): ("auto", "True", "False"),
    
    ("NuSVR", "kernel"): ("linear", "poly", "rbf", "sigmoid", "precomputed"),
    # ("NuSVR", "gamma"): ("scale", "auto", float),
    
    ("SVR", "kernel"): ("linear", "poly", "rbf", "sigmoid", "precomputed"),
    # ("SVR", "gamma"): ("scale", "auto", float),
    
    ("KNeighborsRegressor", "weights"): ("uniform", "distance",  ),
    ("KNeighborsRegressor", "algorithm"): ("auto", "ball_tree", "kd_tree", "brute"),
    ("KNeighborsRegressor", "metric"): ("minkowski", "euclidean", "manhattan", "chebyshev", "mahalanobis"), # and others
    
    ("RadiusNeighborsRegressor", "weights"): ("uniform", "distance",  ),
    ("RadiusNeighborsRegressor", "algorithm"): ("auto", "ball_tree", "kd_tree", "brute"),
    ("RadiusNeighborsRegressor", "metric"): ("minkowski", "euclidean", "manhattan"),
    
    ("LogisticRegression", "penalty"): ("l2", "l1", "elasticnet",  "None"),
    ("LogisticRegression", "solver"): ("lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag", "saga"),
    
    ("RidgeClassifier", "solver"): ("auto", "svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga", "lbfgs"),
    
    ("PassiveAggressiveClassifier", "loss"): ("hinge", "squared_hinge"),
    
    ("SGDClassifier", "loss"): ("hinge", "log_loss", "modified_huber", "squared_hinge", "perceptron", "squared_error", "huber", "epsilon_insensitive", "squared_epsilon_insensitive"),
    ("SGDClassifier", "penalty"): ("l2", "l1", "elasticnet",  "None"),
    ("SGDClassifier", "learning_rate"): ("constant", "optimal", "invscaling", "adaptive"),
    
    ("DummyClassifier", "strategy"): ("most_frequent", "prior", "stratified", "uniform", "constant"),
    
    ("ExtraTreesClassifier", "criterion"): ("gini", "entropy", "log_loss"),
    # ("ExtraTreesClassifier", "max_features"): ("sqrt", "log2",  "None", int, float),
    
    ("GradientBoostingClassifier", "loss"): ("log_loss", "exponential"),
    ("GradientBoostingClassifier", "criterion"): ("friedman_mse", "squared_error"),
    
    ("HistGradientBoostingClassifier", "loss"): ("log_loss",),
    ("HistGradientBoostingClassifier", "categorical_features"): ("from_dtype", "warn",  "None", "array-like"),
    ("HistGradientBoostingClassifier", "early_stopping"): ("auto", "True", "False"),
    ("HistGradientBoostingClassifier", "scoring"): ("loss", "accuracy", "balanced_accuracy", "roc_auc",  "None"),
    
    ("RandomForestClassifier", "criterion"): ("gini", "entropy", "log_loss"),
    # ("RandomForestClassifier", "max_features"): ("sqrt", "log2",  "None", int, float),
    
    ("MLPClassifier", "activation"): ("identity", "logistic", "tanh", "relu"),
    ("MLPClassifier", "solver"): ("lbfgs", "sgd", "adam"),
    # ("MLPClassifier", "batch_size"): ("auto", int),
    ("MLPClassifier", "learning_rate"): ("constant", "invscaling", "adaptive"),
    
    ("DecisionTreeClassifier", "criterion"): ("gini", "entropy", "log_loss"),
    ("DecisionTreeClassifier", "splitter"): ("best", "random"),
    
    ("ExtraTreeClassifier", "criterion"): ("gini", "entropy", "log_loss"),
    ("ExtraTreeClassifier", "splitter"): ("best", "random"),
    # ("ExtraTreeClassifier", "max_features"): ("sqrt", "log2", None, int, float),
    
    ("LinearSVC", "penalty"): ("l1", "l2"),
    ("LinearSVC", "loss"): ("hinge", "squared_hinge"),
    ("LinearSVC", "dual"): ("auto", "True", "False"),
    ("LinearSVC", "multi_class"): ("ovr", "crammer_singer"),
    
    ("NuSVC", "kernel"): ("linear", "poly", "rbf", "sigmoid", "precomputed"),
    # ("NuSVC", "gamma"): ("scale", "auto", float),
    ("NuSVC", "decision_function_shape"): ("ovr", "ovo"),
    
    ("SVC", "kernel"): ("linear", "poly", "rbf", "sigmoid", "precomputed"),
    # ("SVC", "gamma"): ("scale", "auto", float),
    ("SVC", "decision_function_shape"): ("ovr", "ovo"),
    
    ("KNeighborsClassifier", "weights"): ("uniform", "distance",  ),
    ("KNeighborsClassifier", "algorithm"): ("auto", "ball_tree", "kd_tree", "brute"),
    ("KNeighborsClassifier", "metric"): ("minkowski", "euclidean", "manhattan", "chebyshev"),
    
    ("RadiusNeighborsClassifier", "weights"): ("uniform", "distance",  ),
    ("RadiusNeighborsClassifier", "algorithm"): ("auto", "ball_tree", "kd_tree", "brute"),
    ("RadiusNeighborsClassifier", "metric"): ("minkowski", "euclidean", "manhattan"),
    
    ("KMeans", "init"): ("k-means++", "random", "array-like"),
    # ("KMeans", "n_init"): ("auto", int),
    ("KMeans", "algorithm"): ("lloyd", "elkan"),
    
    ("BisectingKMeans", "init"): ("k-means++", "random"),
    ("BisectingKMeans", "algorithm"): ("lloyd", "elkan"),
    ("BisectingKMeans", "bisecting_strategy"): ("biggest_inertia", "largest_cluster"),
    
    ("Normalizer", "norm"): ("l1", "l2", "max"),
    
    ("PolynomialFeatures", "order"): ("C", "F"),
    
    ("PowerTransformer", "method"): ("yeo-johnson", "box-cox"),
    ("QuantileTransformer", "output_distribution"): ("uniform", "normal"),
    ("SplineTransformer", "knots"): ("uniform", "quantile", "array-like"),
    ("SplineTransformer", "extrapolation"): ("constant", "linear", "periodic"),
    ("SplineTransformer", "order"): ("C", "F"), # Refers to memory layout
    ("SplineTransformer", "handle_missing"): ("error", "drop")
}
