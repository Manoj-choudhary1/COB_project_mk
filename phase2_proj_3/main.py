import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Replace 'your_dataset_url' with the actual URL where your dataset is located
dataset_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTSS-TcErkXNk8KB0AlijhitwetxeHD2M3R0HJl2QPMAyFq0fxFX4PFKnzAWLDnratIz67DNL6GsZnV/pub?output=csv'

# Load the dataset
df = pd.read_csv(dataset_url)

# Display the first few rows of the dataset
print("Dataset Overview:")
print(df.head())


# Pairplot to visualize relationships between numerical columns
sns.pairplot(df)
plt.title('Pairplot of Dataset')
plt.show()

# Correlation heatmap
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# Boxplot to identify outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, orient='h', palette='Set2')
plt.title('Boxplot of Numerical Columns')
plt.show()

# Histograms for numerical columns
plt.figure(figsize=(12, 8))
df.hist(edgecolor='black', linewidth=1.2)
plt.suptitle('Histograms of Dataset', x=0.5, y=1.02, ha='center', fontsize='large')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
