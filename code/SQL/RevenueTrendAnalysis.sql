SELECT
    DATE_FORMAT(order_date,'%Y-%m') AS month,
    SUM(amount) AS revenue
FROM transactions
GROUP BY month
ORDER BY month;
