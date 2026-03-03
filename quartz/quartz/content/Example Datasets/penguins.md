![[Pasted image 20260218201955.png]]

Penguins! They're fluffy! They're cuddly! Whats not to like? 

The **Palmer Penguins** dataset is a collection of biological measurements for three penguin species found in the Palmer Archipelago, Antarctica. It has become the gold standard for teaching data science.

### Dataset Structure

The curated version of the dataset contains **344 observations** across **8 variables**:

| **Variable**       | **Type**         | **Description**                                |
| ------------------ | ---------------- | ---------------------------------------------- |
| **Species**        | Categorical      | Adélie, Chinstrap, or Gentoo                   |
| **Island**         | Categorical      | Biscoe, Dream, or Torgersen                    |
| **Bill Length**    | Numerical ($mm$) | Length of the upper ridge of the beak (culmen) |
| **Bill Depth**     | Numerical ($mm$) | Vertical thickness of the beak                 |
| **Flipper Length** | Numerical ($mm$) | Length of the penguin's flipper                |
| **Body Mass**      | Numerical ($g$)  | Total weight of the penguin                    |
| **Sex**            | Categorical      | Male or Female                                 |
| **Year**           | Numerical        | Year of study (2007, 2008, or 2009)            |

>[!question] Lab Questions
> 1. What is the relationship between flipper_length_mm and body_mass_g? 
> 2. Create a linear AI model that takes in flipper_length_mm and body_mass_g as inputs, and predicts the gender of the penguins. 
> 3. Which is a better predictor of gender? year or bill_length? 

### Dataset Source
The data was collected by **Dr. Kristen Gorman** and the **Palmer Station, Antarctica LTER** (Long Term Ecological Research) Program. It was originally published as part of a 2014 study on the foraging behavior and environmental variability of Antarctic penguins.
[Link](https://cran.r-project.org/web/packages/palmerpenguins/readme/README.html)