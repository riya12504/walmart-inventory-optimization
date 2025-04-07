#📌 Walmart-Inventory-Optimization

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load the dataset (replace 'Walmart.xlsx' with your file path)
df = pd.read_excel("C:/Users/Administrator/OneDrive/Desktop/Projects/sales/Walmart/Data/walmart Retail Data.xlsx", engine='openpyxl')

# Display the first few rows to check the data
print(df.head())
# Overview of the data
df.info()

# Handle missing values (forward fill)
df.ffill(inplace=True)  # Fixed the deprecated fillna() warning

# Remove duplicates
df.drop_duplicates(inplace=True)
# Calculate Total Sales and Total Profit
df['Total Sales'] = df['Sales'] * df['Order Quantity']
df['Total Profit'] = df['Profit'] * df['Order Quantity']

# Summary of total sales and profit
print(df[['Total Sales', 'Total Profit']].describe())

# Plot Total Sales Over Time
df.groupby('Order Date')['Total Sales'].sum().plot(figsize=(12,6), title="Total Sales Over Time")
plt.show()
# Calculate the average weekly sales
average_weekly_sales = df.groupby('Order Date')['Total Sales'].mean().mean()

# Assume a 2-week lead time for reorder
lead_time = 2  # weeks
reorder_point = average_weekly_sales * lead_time

print(f"Reorder Point (ROP) = {reorder_point}")

# Assuming some values for costs
ordering_cost = 50
holding_cost = 5

# Calculate EOQ
EOQ = np.sqrt((2 * average_weekly_sales * ordering_cost) / holding_cost)
print(f"Economic Order Quantity (EOQ) = {EOQ}")

