import csv

# Data to be written to the CSV file
data = [
    ["Feature", "Variable Type", "Variable", "Value Type"],
    ["Age", "Objective Feature", "age", "int (days)"],
    ["Height", "Objective Feature", "height", "int (cm)"],
    ["Weight", "Objective Feature", "weight", "float (kg)"],
    ["Gender", "Objective Feature", "gender", "categorical code"],
    ["Systolic blood pressure", "Examination Feature", "ap_hi", "int"],
    ["Diastolic blood pressure", "Examination Feature", "ap_lo", "int"],
    ["Cholesterol", "Examination Feature", "cholesterol", "1: normal, 2: above normal, 3: well above normal"],
    ["Glucose", "Examination Feature", "gluc", "1: normal, 2: above normal, 3: well above normal"],
    ["Smoking", "Subjective Feature", "smoke", "binary"],
    ["Alcohol intake", "Subjective Feature", "alco", "binary"],
    ["Physical activity", "Subjective Feature", "active", "binary"],
    ["Presence or absence of cardiovascular disease", "Target Variable", "cardio", "binary"]
]

# Specify the file name
filename = "medical_examination.csv"

# Writing to CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'medical_examination.csv' created successfully!")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (df['BMI'] > 25).astype(int)
df.drop('BMI', axis=1, inplace=True)

# Normalize data by making 0 always good and 1 always bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt`
    df_cat = pd.melt(df, id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data
    df_cat = df_cat.value_counts().reset_index(name='total').sort_values(by=['cardio', 'variable', 'value'])

    # Draw the catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat).fig

    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, square=True, linewidths=.5, cbar_kws={"shrink": 0.5})

    return fig
