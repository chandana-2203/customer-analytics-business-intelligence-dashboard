import matplotlib.pyplot as plt

monthly = (
    df.groupby("month")["amount"]
    .sum()
)

plt.figure(figsize=(10,5))
monthly.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
