import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
file_path = 'data.csv'
df = pd.read_csv('C:\\Users\\navee\Downloads\Data.csv')

# Display the first few rows of the dataframe
print("First few rows of the data:")
print(df.head())

# Display summary statistics
print("\nSummary statistics:")
print(df.describe())
