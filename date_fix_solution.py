import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv('data/Assessment-2-Associate-DS(in).csv')

print("Original data shape:", df.shape)
print("\nSample of weekend_date values:")
print(df['weekend_date'].head(10).tolist())

df['weekend_date'] = pd.to_datetime(df['weekend_date'], dayfirst=True)

print("\nDate conversion successful!")
print("Sample converted dates:")
print(df['weekend_date'].head(10))
print(f"\nDate range: {df['weekend_date'].min()} to {df['weekend_date'].max()}")

# Now you can create your weekly sales aggregation
weekly_sales = df.groupby('weekend_date')['quantity'].sum()
print("\nWeekly sales aggregation:")
print(weekly_sales.head(10))

# Create the plot
plt.figure(figsize=(12,6))
plt.plot(weekly_sales.index, weekly_sales.values, marker='o', linewidth=2, markersize=4)
plt.title('Weekly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nAlternative solutions if dayfirst=True doesn't work:")

# Use format parameter with mixed format
print("\nAlternative 1: Using format='mixed'")
try:
    df_alt1 = pd.read_csv('data/Assessment-2-Associate-DS(in).csv')
    df_alt1['weekend_date'] = pd.to_datetime(df_alt1['weekend_date'], format='mixed', dayfirst=True)
    print("Alternative 1 works!")
except Exception as e:
    print(f"Alternative 1 failed: {e}")

#  Manual date parsing
print("\nAlternative 2: Manual parsing with custom function")
def parse_date(date_str):
    """Custom function to parse dates in day/month/year format"""
    try:
        # Remove time component if present
        date_str = date_str.split()[0]
        return pd.to_datetime(date_str, format='%d/%m/%Y')
    except:
        try:
            return pd.to_datetime(date_str, format='%d/%m/%Y')
        except:
            return pd.NaT

df_alt2 = pd.read_csv('data/Assessment-2-Associate-DS(in).csv')
df_alt2['weekend_date'] = df_alt2['weekend_date'].apply(parse_date)
print("Alternative 2 works!")
print("Sample dates:", df_alt2['weekend_date'].head(5).tolist()) 