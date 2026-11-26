"""
## Reflection
1. Without looking at your code, can you explain what a boolean filter does in plain English? Practice saying it out loud.
A boolean filter tests every row against a True/False condition and keeps only the rows that evaluate to True.

2. What is the difference between df["revenue"] and df[["revenue"]]? When does the distinction matter?
df["revenue"] returns a 1D Series, while df[["revenue"]] returns a 2D DataFrame. It matters when selecting multiple columns or passing data to functions and models that require a 2D table.

3. If a colleague who only knows Excel asked you to explain why you would choose pandas for this task, what is the single most compelling reason you would give?
Because I prioritize automation, I only need to write the script once and can re-run it on new files in seconds without manual clicking or altering the raw data.
"""
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
# EXERCISE 3: Top 5 by revenue
print("\n--- EXERCISE 3 ---")
top_5_revenue = df.sort_values('revenue', ascending=False).head(5)
print(top_5_revenue)
# EXERCISE 4: Two-condition filter
print("\n--- EXERCISE 4 ---")
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print("Big South row count:", len(big_south))
print(big_south.head())
# EXERCISE 5: A new column
print("\n--- EXERCISE 5 ---")
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print("Mean per-unit price:", df['per_unit'].mean())
# EXERCISE 6: Unique values
print("\n--- EXERCISE 6 ---")
print("Unique regions:", df['region'].unique())
print("Region value counts:\n", df['region'].value_counts())
# EXERCISE 7: Select columns
print("\n--- EXERCISE 7 ---")
subset_df = df[['region', 'product', 'revenue']]
print("Subset shape:", subset_df.shape)
# EXERCISE 8: Save
print("\n--- EXERCISE 8 ---")
df.to_csv('data/explored.csv', index=False)
print("Saved data/explored.csv successfully!")