
Support Vector Machines for regression (SVR) work by finding a hyperplane in a high-dimensional space that best fits the data. Unlike traditional linear regression, which tries to minimize the error between the prediction and the data point, SVR tries to fit the best line within a predefined threshold (epsilon-tube) of error.
#### Pros of SVM:

* Provides non-linear modeling.
* semi resistant to over fitting. 

#### Cons of SVM:

* Does not directly provide probability estimates.
* Can be computationally expensive on large datasets.

# Regressors

| Model Name | **Summary** | **Link to sklearn-documentation** |
| --- | --- | --- |
| **LinearSVR** | Similar to SVR with a linear kernel but implemented via `liblinear` rather than `libsvm`. It scales better to large numbers of samples and provides more flexibility in loss functions and regularization. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html) |
| **NuSVR** | A variation of SVR that uses a parameter $\nu$ (nu) to control the number of support vectors. It is mathematically equivalent to SVR but uses a different parameterization to bound the fraction of training errors. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html) |
| **SVR** | The standard Epsilon-Support Vector Regression. It uses a "tube" of insensitivity where errors are ignored if they are smaller than a specified $\epsilon$, allowing for non-linear fit via kernels (like RBF or Polynomial). | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html) |
# Classifiers

| Model Name | **Summary** | **Link to sklearn-documentation** |
| --- | --- | --- |
| **LinearSVC** | Similar to SVC with a `kernel='linear'`, but implemented via `liblinear`. It is faster, scales better to large datasets, and supports more flexibility in loss functions and penalty types. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html) |
| **NuSVC** | Similar to SVC but uses a parameter $\nu$ (nu) to control the number of support vectors. The parameter $\nu$ represents an upper bound on the fraction of margin errors and a lower bound of the fraction of support vectors. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html) |
| **SVC** | The C-Support Vector Classification. It uses a penalty parameter $C$ to handle the trade-off between maximizing the margin and minimizing misclassifications. It supports non-linear kernels like RBF, Poly, and Sigmoid. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) |
