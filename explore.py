import pandas as pd
# EXERCISE 1: Load it
df = pd.read_csv('data/retail_sales.csv')
print("--- EXERCISE 1 ---")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data types:\n", df.dtypes)
# EXERCISE 2: Filter by region
print("\n--- EXERCISE 2 ---")
south = df[df['region'] == 'South']
print("South row count:", len(south))
print(south.head())