### Tree Models
Tree models predict values by recursively partitioning data into subsets based on feature thresholds, creating a structure that resembles an upside-down tree. Each internal node represents a decision point, while the terminal "leaves" provide the final numerical prediction or category. Their main appeal lies in their interpretability and their ability to capture complex, non-linear relationships without requiring extensive data preprocessing.
#### Pros tree models:
* Can understand non-linear and complex relationships.
#### Cons tree models:
* Very Prone to over fitting
# Regressors

| Model Name                | **Summary**                                                                                                                                                                                                   | **Link to sklearn-documentation**                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **DecisionTreeRegressor** | A non-parametric supervised learning method that predicts a continuous target value by learning simple decision rules (if-then-else) inferred from the data features.                                         | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html) |
| **ExtraTreeRegressor**    | An extremely randomized tree regressor that introduces additional randomness by choosing a split point at random for each feature instead of searching for the optimal threshold, helping to reduce variance. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html)    |
