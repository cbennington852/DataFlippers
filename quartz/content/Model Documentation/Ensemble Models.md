
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
