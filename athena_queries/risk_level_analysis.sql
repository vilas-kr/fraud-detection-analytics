SELECT 
    risk_level, 
    COUNT(*) as transactions
FROM fraud_processed
GROUP BY risk_level;
