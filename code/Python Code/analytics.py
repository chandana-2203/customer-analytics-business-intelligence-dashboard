import pandas as pd

df = pd.read_csv("data/customer_transactions.csv")

total_revenue = df["amount"].sum()

average_order_value = df["amount"].mean()

unique_customers = df["customer_id"].nunique()

print("Revenue:", total_revenue)
print("Average Order:", average_order_value)
print("Customers:", unique_customers)
