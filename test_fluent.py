import pandas as pd


df = pd.read_csv("resources/loan_data.csv")

print(df)

mean_income = 100000


import numpy as np

def calculate_realistic_income(row):
    # 1. Set Base Income by Zip Code Group
    if row['Zip_Code_Group'] == 'Urban Professional':
        income = np.random.normal(95000, 15000)
    elif row['Zip_Code_Group'] == 'High-income Suburban':
        income = np.random.normal(110000, 20000)
    elif row['Zip_Code_Group'] == 'Working Class Urban':
        income = np.random.normal(45000, 8000)
    else: # Historically Redlined / Other
        income = np.random.normal(38000, 7000)

    # 2. Apply the Criminal Record Penalty (The "Accurate" Part)
    if row['Criminal_Record'] == 'Yes':
        # Apply a 30% reduction with a bit of randomness
        penalty = np.random.uniform(0.25, 0.40) 
        income = income * (1 - penalty)

    return round(income, 2)

# Apply to your dataframe
df['Annual_Income'] = df.apply(calculate_realistic_income, axis=1)
