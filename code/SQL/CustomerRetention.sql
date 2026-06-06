SELECT
    customer_id,
    COUNT(DISTINCT DATE_FORMAT(order_date,'%Y-%m')) AS active_months
FROM transactions
GROUP BY customer_id
ORDER BY active_months DESC;
