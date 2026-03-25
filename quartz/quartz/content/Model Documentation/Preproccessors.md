Preproccessors let us change the input data for each model. 

__Lessons on this topic__
* [[7. Preproccessors]]
### **Scalar Preprocessors**

These tools adjust the scale and distribution of your numeric features to improve model performance.

|**Model**|**2-Sentence Explanation**|**Link to sklearn-documentation**|
|---|---|---|
|**MaxAbsScaler**|It scales each feature by its maximum absolute value so that the data resides within the range $[-1, 1]$. This is specifically designed to preserve the sparsity of data (like matrices full of zeros).|[Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)|
|**MinMaxScaler**|This scales features to a user-defined range, usually $[0, 1]$, based on the minimum and maximum values. It is easy to interpret but can be heavily distorted if your data contains extreme outliers.|[Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)|
|**RobustScaler**|It removes the median and scales data according to the Interquartile Range (IQR). Because it ignores extreme values, it is the best choice for datasets that contain significant outliers.|[Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html)|
|**StandardScaler**|This transforms data to have a mean of 0 and a standard deviation of 1. It is the most common scaler but assumes your data follows a normal (Gaussian) distribution.|[Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)|
|**Normalizer**|Unlike other scalers, this operates on each sample (row) rather than each feature (column). It ensures each row has a "unit norm," which is vital for text classification and distance-based clustering.|[Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html)|
|**PowerTransformer**|This applies a power transformation to make data more "Gaussian-like" and stabilize variance across the dataset. It is highly effective for correcting skewed data or non-constant variance (heteroscedasticity).|[Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html)|
|**QuantileTransformer**|It uses quantiles to map data to a uniform or normal distribution, spreading out the most frequent values. This reduces the impact of marginal outliers but may break linear relationships between variables.|[Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html)|
### **Cluster Preprocessors**

These models are used to group data points together, which can then be used as new features for a downstream model.

|**Model**|**2-Sentence Explanation**|**Documentation Link**|
|---|---|---|
|**KMeans**|It partitions data into $K$ clusters by minimizing the distance between points and their respective cluster centroids. This is a fast, efficient baseline but requires you to choose the number of clusters (K) beforehand.|[Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)|
|**Birch**|This memory-efficient algorithm builds a tree structure to represent data, making it ideal for very large datasets. It can cluster data in a single pass, which is helpful when computing resources are limited.|[Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html)|
|**BisectingKMeans**|A hierarchical variation of KMeans that starts with one cluster and repeatedly splits them into two until the target number is reached. It often produces more stable and well-separated clusters than standard KMeans.|[Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html)|

### **Feature Generators**

These generate new synthetic features based on your existing data to capture more complex patterns.

| **Model**              | **2-Sentence Explanation**                                                                                                                                                                                               | **Documentation Link**                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **PolynomialFeatures** | This creates new features by generating all possible polynomial combinations of the original variables up to a set degree. It allows simple linear models to learn "curves" and interactions between different features. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html) |
| **SplineTransformer**  | It generates a B-spline basis for features, allowing for flexible non-linear modeling of data. This is often more stable and local than polynomial features, which can behave erratically at the edges of data ranges.   | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html)  |

---

Would you like me to help you write a code snippet to visualize how these different **Scalars** affect a specific dataset?