
|                                      | **Regression**                                                                                                                                                                      |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**                      | Takes in any combination of input data, and outputs a prediction in the form of a number.<br><br>Example:<br>- Input: `bill_length_mm = 39.1` <br>- Output: `bill_depth_mm = 181.0` |
| **Prediction data type**             | Numerical                                                                                                                                                                           |
| **Ways to assess model performance** | - RMSE (Root Mean Squared Error)<br>- Explained Varience<br>- $R^2$                                                                                                                 |
## Understanding Regression Accuracy
The accuracy graph for the regressor shows the explained accuracy for each data point. The dotted red line represents a *perfect* prediction. The Y axis(Predicted Values) shows the models predictions, and the X axis(Actual Values) shows the actual values reflected in the training dataset. 

This means, the closer the blue dots are to the red line, the better our AI model is performing! 
![[regressor_accuracy.png]]




### Neural Networks
The MLPRegressor (Multi-layer Perceptron Regressor) is a neural network model that learns a non-linear function for regression by training on datasets using backpropagation. It consists of at least three layers and utilizes activation functions like ReLU or Logistic to model complex dependencies. Unlike linear regressors, it can capture intricate patterns, though it requires careful tuning of hyperparameters and feature scaling to perform optimally.

#### Pros neural networks:
* Can understand very very complex relationships. 
* Semi-resilient to over fitting. 
#### Cons neural networks:
* Very very slow to train
* requires tuning of [[Model Hyper Parameters]] to reach full potential. 

| Model Name | **Summary** | **Link to sklearn-documentation** |
| --- | --- | --- |
| **MLPRegressor** | A supervised learning algorithm that trains using backpropagation over multiple layers of nodes (neurons) to predict continuous outputs through non-linear transformations. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html) |