SELECT device_type, COUNT(*)
FROM device_data 
WHERE fraud_flag = 1 
GROUP BY device_type; 