![[Pasted image 20260219080848.png]]

Time to stop and smell the flowers! Or was is roses?

This dataset features flowers, and their measurements. Its a popular introductory dataset for data science, and by extension machine learning. 

### Dataset Structure

| **Attribute**    | **Type**         | **Description**                                                          |
| ---------------- | ---------------- | ------------------------------------------------------------------------ |
| **Sepal Length** | Numerical ($cm$) | The length of the outer leaf-like part of the flower.                    |
| **Sepal Width**  | Numerical ($cm$) | The width of the outer leaf-like part of the flower.                     |
| **Petal Length** | Numerical ($cm$) | The length of the inner, often colorful, flower petals.                  |
| **Petal Width**  | Numerical ($cm$) | The width of the inner, often colorful, flower petals.                   |
| **Species**      | Categorical      | The specific Iris species: **Setosa**, **Versicolor**, or **Virginica**. |

> [!question] Lab Questions
> 1. Plot sepal_legth vs sepal_width. Then add a random forest regressor and a linear regressor. Does one of them over fit? Which model do you think is better? 
> 2. Plot (sepal_length x species) vs sepal_width. Then add a random forest regressor and a linear regressor. Does one of them over fit? Which model do you think is better? 
> 3. Plot (sepal_length x sepal_width) vs species. Add two MLPclassifiers, one of them with a scalar, and the other without. Which one performs better? 
### Dataset Source
The data was originally published in **1936** by the British statistician and biologist **Sir Ronald A. Fisher**.
[Link](https://archive.ics.uci.edu/ml/datasets/iris)