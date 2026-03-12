CREATE TABLE IF NOT EXISTS creditcard_partitioned
  WITH (
    format='parquet', 
    external_location='s3://vilas-fraud-detection-datalake/partitioned/',
    partitioned_by = ARRAY['class']
    ) AS
SELECT *
FROM creditcard_transactions;