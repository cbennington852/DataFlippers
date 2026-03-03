Upon loading into the app you will be greeted with the main menu. Here you can access example datasets, as well as any recent datasets you have saved on your computer. Each item under the [example datasets](/Example-Datasets/) is clickable, and will open the respective example dataset. 

For this demo click on the [[penguins]] dataset.
![[where_clikc_examples.png]]

After clicking on the [[penguins]] dataset, you will see the main project screen. This represents where you engineer and modify your AI models. 

## Dataframe Basics
Each "row" in the dataset corresponds to an item in that dataset. Since this example is using the [[penguins]] dataset, each row corresponds to a penguin.
![[row_datafrane_item.png]]
Each “Column block” corresponds to a “column” on the dataset you are using! This is how we determine which parts of the dateset are ignored, used as training data, and what we are trying to predict! 
![[collumn_block_to_dataframe (1).png]]

## Plotting and Controls

Okay, lets try some plotting first!
1. Drag and drop the `bill_length_mm` into the inputs section.
2. Drag and drop the `bill_depth_mm` into the outputs section.
3. Click Run! 
![[Pasted image 20260219133435.png]]

Each dot corresponds to a penguin with the respective features. 

![[penguin_point_graph (2).png]]

## First Model : LinearRegression
The simplest AI model in the world! linear regression! This model looks at the data, and finds a straight line that fits the dataset best! 

Lets try it out! 
1. Click on the "[[Regressors]]" tab, this is on the left side of the screen. 
2. Drag the [LinearRegresison](https://developers.google.com/machine-learning/crash-course/linear-regression) to the "model" section on your first pipeline. 
![[Pasted image 20260222080847.png]]

In the plots tab we get the results of our model training! This line is a visual representation of our [LinearRegresison](https://developers.google.com/machine-learning/crash-course/linear-regression) model. Each place on the line corresponds to a respective  prediction from our AI model! 

![[plot_explained.png]]

Hooray! We've trained and plotted our first AI model! 

## Next Steps
* [[Classifiers]]
* [[Regression Versus Classification]]
* [[Predictions]]
* [[Validators]]