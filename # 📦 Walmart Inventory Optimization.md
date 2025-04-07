# 📦 Walmart Inventory Optimization Project

This project analyzes Walmart's retail sales data to extract actionable insights for inventory planning and optimization using Python. The goal is to reduce stockouts, optimize order quantities, and improve operational efficiency.

---

## 📁 Dataset
- **Source:** Internal retail dataset (2012–2016)
- **Format:** Excel (.xlsx)
- **Features:** Order date, product category, sales, profit, order quantity, customer details, shipping mode, and more

---

## 🔧 Tools & Technologies
- **Python** (Pandas, NumPy, Matplotlib)
- **Excel** for data inspection

---

## 🧹 Data Preprocessing
- Handled missing values using forward-fill (`ffill()`)
- Removed duplicate entries
- Created new calculated fields:
  - `Total Sales = Sales × Order Quantity`
  - `Total Profit = Profit × Order Quantity`

---

## 📈 Exploratory Data Analysis
- Plotted daily `Total Sales` over time to understand sales trends
- Aggregated weekly sales to calculate the average

```python
# Plot Total Sales Over Time
df.groupby('Order Date')['Total Sales'].sum().plot(figsize=(12,6), title="Total Sales Over Time")
plt.show()
```

---

## 📊 Inventory Metrics
### ✅ Reorder Point (ROP)
- Calculated using:
  ```
  ROP = Average Weekly Sales × Lead Time (2 weeks)
  ```
- **ROP = 114,047 units**

### ✅ Economic Order Quantity (EOQ)
- Formula:
  ```
  EOQ = sqrt((2 × Demand × Ordering Cost) / Holding Cost)
  ```
- Assumed:
  - Ordering cost = 50
  - Holding cost = 5
- **EOQ ≈ 1,068 units**

---

## 🧠 Interpretation & Business Impact

### 🔍 Key Insights:
- **Seasonal Sales Trends:** Regular spikes point to high sales periods and seasonality.
- **ROP & EOQ:** Help maintain optimal stock levels while minimizing inventory costs.
- **KPI Enhancement:** Created Total Sales & Profit for better business tracking.

### 💡 Business Value:
- Reduces overstock and stockout scenarios
- Improves customer satisfaction
- Lowers overall inventory costs
- Enables proactive procurement decisions

---

## 📂 Project Structure
```
Walmart-Inventory-Optimization/
├── walmart_retail_data.xlsx
├── walmart_inventory_optimization.py
├── README.md
└── Figure_1.png (Sales Trend Visualization)
```

---

## 🔗 Connect with Me
- 👩‍💻 [LinkedIn](https://www.linkedin.com/in/riyanaik07)
- 💻 [More Projects on GitHub](https://github.com/riyanaik07)
