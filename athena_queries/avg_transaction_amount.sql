SELECT 
    class,
    AVG(amount) as avg_transaction
FROM creditcard_transactions
GROUP BY class;
