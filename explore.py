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