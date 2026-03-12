SELECT
    CAST(time/3600 AS INTEGER) AS hour_window,
    COUNT(*) as fraud_count
FROM creditcard_transactions
WHERE class = 1
GROUP BY CAST(time/3600 AS INTEGER)
ORDER BY fraud_count DESC;
