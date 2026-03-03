
These models focus on combining multiple models to improve generalizability and robustness.
#### Pros ensemble models:
* Can understand non-linear and semi-complex relationships.
#### Cons ensemble models:
* Complex
* Longer training time
# Regressors

| Model Name                        | **Summary**                                                                                                                                                                        | **Link to sklearn-documentation**                                                                                      |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **AdaBoostRegressor**             | An adaptive boosting algorithm that fits a sequence of weak learners, adjusting the weights of data points based on previous errors to focus on "hard" cases.                      | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)             |
| **BaggingRegressor**              | Fits multiple versions of a base regressor on different random subsets of the data and averages their predictions to reduce variance.                                              | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html)              |
| **ExtraTreesRegressor**           | "Extremely Randomized Trees" take randomness a step further than Random Forests by choosing split points totally at random for each feature, often reducing variance further.      | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html)           |
| **GradientBoostingRegressor**     | An additive model that builds trees one at a time, where each new tree helps to correct the errors (residuals) made by the previously built trees.                                 | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)     |
| **HistGradientBoostingRegressor** | A highly optimized version of Gradient Boosting that bins continuous input features into integer-valued bins, significantly speeding up training on large datasets ($n > 10,000$). | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html) |
| **RandomForestRegressor**         | A staple of machine learning that fits a forest of decision trees on various sub-samples of the dataset and averages them to control over-fitting.                                 | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)         |
# Classifiers

| Model Name | Summary | Link to Documentation |
| --- | --- | --- |
| **AdaBoostClassifier** | A meta-estimator that begins by fitting a classifier on the original dataset and then fits additional copies of the classifier on the same dataset, where weights of incorrectly classified instances are adjusted. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html) |
| **BaggingClassifier** | Fits base classifiers each on random subsets of the original dataset and then aggregates their individual predictions to form a final prediction. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html) |
| **ExtraTreesClassifier** | Implements a meta estimator that fits a number of randomized decision trees (a.k.a. extra-trees) on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html) |
| **GradientBoostingClassifier** | Builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html) |
| **HistGradientBoostingClassifier** | A much faster variant of Gradient Boosting for large datasets (n > 10,000), which bins continuous input features into discrete integer-valued bins. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html) |
| **RandomForestClassifier** | A meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) |
