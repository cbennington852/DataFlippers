DataScratch supports a total of three validators. These are used to validate that your model is accurate, and accommodate for over fitting. 

__Lessons on this topic__
* [[8. Validators]]

| Validator Name      | **Summary**                                                                                                                                                       | **Link to sklearn-documentation**                                                                               |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **KFold**           | Splits the dataset into $k$ consecutive folds. Each fold is used once as a validation set while the remaining $k-1$ folds form the training set.                  | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html)           |
| **StratifiedKFold** | A variation of KFold that ensures each fold has the **same proportion of class labels** as the entire dataset. Essential for imbalanced classification tasks.     | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html) |
| **LeaveOneOut**     | Each learning set is created by taking all the samples except one, the remaining sample being the test set. For $n$ samples, we have $n$ different training sets. | [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html)     |

