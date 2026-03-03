![[Pasted image 20260219124834.png]]

A completely random dataset, for the purpose of teaching concepts like over fitting and other things. There is no correlation anywhere. Every column is uniformly random. 

### Dataset Structure

| **Attribute**         | **Type**  | **Description** |
| --------------------- | --------- | --------------- |
| **Random Chemical 1** | Numerical | Random values   |
| **Random Chemical 2** | Numerical | Random values   |
| **Random Chemical 3** | Numerical | Random values   |
| **Random Chemical 4** | Numerical | Random values   |
|                       |           |                 |
 >[!question] Lab Questions
> 1. Train the DecisionTreeReggresor on any two columns. What is the accuracy? Is the model [overfitting](https://developers.google.com/machine-learning/crash-course/overfitting/overfitting)? If you add a validator(like KFold) what happens to the accuracy?
> 2. Train the RandomForestRegressor on any two columns. Modify the hyper parameters `n_estimator`, change it to 1, 10, and 10000. Which parameter overfits the most? 
> 3. Train the DecisionTreeReggresor on any two columns. Modify the hyper parameters `max_depth`, change it to 3, 5, and 1000. How does this change the model? 

### Dataset Source
python's [random function](https://docs.python.org/3/library/random.html). 