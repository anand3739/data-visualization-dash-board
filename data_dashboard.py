import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV
df = pd.read_csv("sales_data.csv")

# 1. Bar Chart – Product vs Sales
plt.figure(figsize=(8, 5))
sns.barplot(x="Product", y="Sales", data=df)
plt.title("Sales per Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.savefig("sales_bar_chart.png")
plt.close()

# 2. Line Chart – Product vs Satisfaction
plt.figure(figsize=(8, 5))
sns.lineplot(x="Product", y="Satisfaction", data=df, marker="o")
plt.title("Customer Satisfaction")
plt.xlabel("Product")
plt.ylabel("Satisfaction Rating")
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig("satisfaction_line_chart.png")
plt.close()

print("✅ Charts generated: 'sales_bar_chart.png', 'satisfaction_line_chart.png'")
