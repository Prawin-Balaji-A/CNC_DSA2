import pandas as pd
import numpy as np
from scipy.stats import zscore

# Load the CSV file
csv_path = "your_file.csv"
df = pd.read_csv(csv_path)

print("\n✅ CSV Loaded Successfully!\n")

# Show missing values
print("Missing Values:\n", df.isnull().sum())

# Fill missing numerical values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill missing categorical values with mode
for col in df.select_dtypes(include='object'):
    df[col].fillna(df[col].mode()[0], inplace=True)

# Remove outliers using Z-score method
numeric_df = df.select_dtypes(include=np.number)
z_scores = np.abs(zscore(numeric_df))
df_clean = df[(z_scores < 3).all(axis=1)]

print("\nShape Before Cleaning:", df.shape)
print("Shape After Cleaning:", df_clean.shape)

# Optionally save cleaned data
df_clean.to_csv("cleaned_data.csv", index=False)
print("\n✅ Cleaned data saved as 'cleaned_data.csv'")
