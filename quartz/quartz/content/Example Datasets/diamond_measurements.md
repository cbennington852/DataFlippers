![[Pasted image 20260218200805.png]]

There are many different types of diamonds in today's world, this dataset features the measurements and prices of over 54,000 diamonds. 

This is the largest example dataset in the DataScratch collection, at a whopping 2.9 mb. This dataset represents a real world scenario that your average data scientist might encounter. 

### Dataset Structure
It contains the classic Four Cs of diamond grading, along with physical dimensions that allow for advanced feature engineering.

| **Attribute**  | **Description**                              | **Values / Scale**                                |
| -------------- | -------------------------------------------- | ------------------------------------------------- |
| **Cut**        | Quality of the diamond's cut and finish.     | Fair, Good, Very Good, Premium, Ideal             |
| **Color**      | The diamond's hue (degree of colorlessness). | **J** (worst/yellowish) to **D** (best/colorless) |
| **Clarity**    | Absence of inclusions or blemishes.          | **I1** (worst) to **IF** (Internally Flawless)    |
| **Carat**      | The physical weight of the diamond.          | Range: 0.2–5.01 $g$                               |
| **Dimensions** | The physical size measurements.              | **x** (length), **y** (width), **z** (depth)      |


> [!question] Lab Questions
> 1. Which column metric has the strongest correlation to price? 
> 2. Which cut has the best price (on average)
> 3. Are most diamonds high value or low value? 

### Dataset Source
This is one of the example datasets from the [seaborn](https://seaborn.pydata.org/) library. It can be accessed [here](https://github.com/mwaskom/seaborn-data/blob/master/diamonds.csv)