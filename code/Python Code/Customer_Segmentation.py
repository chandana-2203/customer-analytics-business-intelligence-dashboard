customer_summary = (
    df.groupby("customer_id")
    .agg({
        "amount": "sum",
        "transaction_id": "count"
    })
)

customer_summary.columns = [
    "total_spent",
    "total_orders"
]

customer_summary["segment"] = customer_summary[
    "total_spent"
].apply(
    lambda x:
    "Premium" if x > 5000
    else "Regular"
)
