# Importing your own training data
To import your own training data, start by clicking on the "import dataset" button from the main menu. Supported file types are excel, csv, parquet. 
![[import button.png]]
# Importing data for model Predictions
The DataScratch models allow for you to input your own predications. This can be accessed after training one or more pipelines. This is accessed from the predications tab. 
![[Pasted image 20260301124619.png]]
## Single Value Predictions
![[Pasted image 20260301124713.png]]
You can do single value predictions. Enter in the values for each predication, and then click predict to see the results. 
![[Pasted image 20260301125516.png]]

## Multiple Predictions
You can import your own dataset to have the models run predictions on. This dataset must be in .csv .xlsx or .parquet format. 

1. Train a model
2. Select multiple values tab ![[Pasted image 20260302095744.png]]
3. Upload a dateset.
![[Pasted image 20260302095911.png]]
4. Click run

The dataset with the predictions will appear on the right. This dateset contains each input value, and each predication from each pipeline plus the name of the output column.  