![[Pasted image 20260323094037.png]]


This dataset is geared twords teaching about algorithmic bias, as well as some basic financial literacy. 
### Dataset Structure

| Attribute                | Type                | Description                                                            |
| :----------------------- | :------------------ | :--------------------------------------------------------------------- |
| **ID**                   | Categorical/Numeric | Unique identifier for each individual entry.                           |
| **Gender**               | Categorical         | Gender of the applicant (Female, Male, Other).                         |
| **Race**                 | Categorical         | Self-identified racial group (White, Hispanic, Other, etc.).           |
| **Age**                  | Numerical           | Age of the individual in years (Range: 18–82).                         |
| **Age_Group**            | Categorical         | Age categorized into specific brackets (e.g., 25–60, Over 60).         |
| **Income**               | Numerical           | Annual income in USD (e.g., 25,000 – 175,000).                         |
| **Credit_Score**         | Numerical           | Creditworthiness score (Range: 500 – 849).                             |
| **Loan_Amount**          | Numerical           | Amount requested for the loan (e.g., 50,100 – 450,000).                |
| **Employment_Type**      | Categorical         | Employment status (Full-time, Part-time, Other).                       |
| **Education_Level**      | Categorical         | Highest qualification (High School, Bachelor’s, Graduate, etc.).       |
| **Citizenship_Status**   | Categorical         | Legal status (Citizen, Permanent Resident, Other).                     |
| **Language_Proficiency** | Categorical         | Language fluency level (Fluent, Limited).                              |
| **Disability_Status**    | Categorical         | Disability indicator (True, False).                                    |
| **Criminal_Record**      | Categorical         | Whether the applicant has a criminal record (True, False).             |
| **Zip_Code_Group**       | Categorical         | Geodemographic area (e.g., High-income Suburban, Working Class Urban). |
| **Loan_Approved**        | Categorical         | Target variable for prediction (APPROVED or DENIED).                   |
 >[!question] Lab Questions
> 1. Which employment type has the highest salary on average? 
### Dataset Source
This is a synthetic dataset for the purpose of teaching & education. It was made by Abbas Rianat and 1 collaborator. It can be found on [kaggle](https://www.kaggle.com/datasets/abbasrianat/financial-loan-access-dataset). This dataset from kaggle was then significantly modified by Charles Bennington.

The image is from Wikipedia. [image source link](https://en.wikipedia.org/wiki/Bank).