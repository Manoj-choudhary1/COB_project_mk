import pandas as pd
import random
from faker import Faker

# Set up Faker for generating synthetic data
fake = Faker()

# Generate synthetic data
num_samples = 100  # You can adjust this based on your requirements

data = {
    'Name': [fake.name() for _ in range(num_samples)],
    'Age': [random.randint(18, 65) for _ in range(num_samples)],
    'City': [fake.city() for _ in range(num_samples)],
    'Salary': [random.randint(30000, 90000) for _ in range(num_samples)]
}

# Create a DataFrame using pandas
dataset = pd.DataFrame(data)

# Display the dataset
print(dataset.head())

# Save the dataset to a CSV file
dataset.to_csv('dataset/sample_dataset.csv', index=False)
