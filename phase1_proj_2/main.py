import pandas as pd
import numpy as np
from scipy import stats

# Load the dataset (replace 'your_dataset_url' with the actual URL)
dataset_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTSS-TcErkXNk8KB0AlijhitwetxeHD2M3R0HJl2QPMAyFq0fxFX4PFKnzAWLDnratIz67DNL6GsZnV/pub?output=csv"
df = pd.read_csv(dataset_url)

# Display the first few rows of the dataset
print("Original Dataset:")
print(df.head())

# Handling missing values
df = df.fillna(method='ffill')  # Forward fill missing values, you can choose another strategy based on your data

# Handling outliers (using Z-score as an example)
z_scores = np.abs(stats.zscore(df.select_dtypes(include=np.number)))
df_no_outliers = df[(z_scores < 3).all(axis=1)]  # Adjust the threshold as needed

# Display the cleaned dataset
print("\nCleaned Dataset:")
print(df_no_outliers.head())

# Save the cleaned dataset to a new CSV file
df_no_outliers.to_csv('cleaned_dataset.csv', index=False)
