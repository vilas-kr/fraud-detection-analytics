SELECT class, COUNT(*) as transaction_count
FROM creditcard_transactions
GROUP BY class;
