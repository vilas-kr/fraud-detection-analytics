# Fraud Detection Analytics using AWS Athena and AWS Glue

## Project Overview
This project demonstrates a serverless data analytics pipeline for fraud detection using AWS S3, AWS Glue, and Amazon Athena.

The goal of the project is to analyze transaction data and identify fraudulent patterns using SQL queries and ETL transformations in a scalable cloud environment.

The pipeline ingests raw transaction data, catalogs it using AWS Glue Crawlers, performs data transformation using Glue ETL, and analyzes fraud patterns using Amazon Athena.

## Architecture
```
Upload to S3 (Raw Layer)
      ↓
Glue Crawler
      ↓
Glue Data Catalog
      ↓
Athena Queries
      ↓
Glue ETL (Risk Level Transformation)
      ↓
S3 Processed Data (Parquet)
      ↓
Athena Analysis
      ↓
Python Script (Athena Automation)
```

## Technologies Used
| Technology	| Purpose |
|------------------|-------------------------------|
| Amazon S3 | Data storage (Data Lake) |
| AWS Glue | Data catalog and ETL processing |
| AWS Glue Crawler | Automatic schema detection |
| Amazon Athena | Serverless SQL analytics |
| Python (Boto3) | Query automation |
| SQL | Data analysis |

## Dataset
The project uses a credit card transaction dataset containing information such as:
- Transaction time
- Transaction amount
- Fraud label (class)
- Additional anonymized features (v1 - v28)

Fraud values:
```
0 -> Normal Transaction
1 -> Fraudulent Transaction
```

Dataset Link:
```
https://www.kaggle.com/datasets/whenamancodes/fraud-detection
``` 

## S3 Data Lake Structure
```
vilas-fraud-detection-datalake
|
|-- transactions/
|   |-- creditcard.csv
|
|-- device-data/
|   |-- transactions.json
|
|-- partitioned/
|   |-- class=0
|   |-- class=1
|
|-- processed-data/
|   |-- fraud_processed
|
|-- query_results/ 
```

## Project Structure
```
fraud-detection-analytics
|
|-- athena/
|   |-- athena_script.py
|
|-- athena_queries/
|   |-- avg_transaction_amount.sql
|   |-- fraud_device_transcation.sql
|   |-- fraud_time_window.sql
|   |-- fraud_vs_normal.sql
|   |-- high_value_fraud.sql
|   |-- partition_by_class.sql
|   |-- risk_level_analysis.sql
|   |-- total_transactions.sql
|
|-- dataset/
|   |-- creditcard.csv
|   |-- transactions.json
|
|-- document/
|   |-- create_crawlers.txt
|   |-- glue_etl.txt
|
|-- glue_jobs/
|   |-- fraud_risk_etl.py
|
|-- screenshots/
|
|-- .gitignore
|-- README.md
|-- requirements.txt
```

## How to Run the Project
Follow the steps below to run the Fraud Detection Analytics pipeline using AWS S3, AWS Glue, and Amazon Athena.

### 1 Clone the Repository
Create a bucket for the project.
```
git clone https://github.com/vilas-kr/fraud-detection-analytics
cd fraud-detection-analytics
```

### 2 Install Python Dependencies
Install the required libraries for running the Athena automation script.
```
pip install -r requirements.txt
```

### 3 Configure AWS Credentials
Configure AWS CLI credentials.
```
aws configure
```
Provide:
```
AWS Access Key ID
AWS Secret Access Key
Region (example: ap-south-1)
Output format: json
```

### 4 Create S3 Data Lake
Create an S3 bucket:
```
fraud-detection-data-lake
```
Create the following folder structure:
```
fraud-detection-data-lake
|
|-- transactions/
|-- processed-data/
|-- device-data/
|-- athena-results/
```
Upload the dataset:
```
dataset/creditcard.csv
dataset/transactions.json
```
to:
```
s3://fraud-detection-data-lake/transactions/creditcard.csv
s3://fraud-detection-data-lake/device-data/transactions.json
```

### 5 Create Glue Crawlers
Glue Crawlers automatically detect dataset schema and create tables in the Glue Data Catalog.

Follow the detailed instructions in:
```
document/create_crawlers.txt
```
This step will create the required Athena queryable tables

### 6 Create Glue ETL Job
Create the AWS Glue ETL job to process transaction data and generate risk-level classifications.

Use the script located at:
```
glue_jobs/fraud_risk_etl.py
```
Detailed instructions are available in:
```
document/glue_etl.txt
```
The ETL job performs:
- Reads transaction dataset from S3
- Adds risk_level column
- Stores processed dataset in Parquet format
Output location:
```
s3://fraud-detection-data-lake/processed-data/
```

### 7 Run Athena Queries
Open Amazon Athena and select the database created by the Glue crawler.

Example queries are available in:
```
athena_queries/
```
Example:
```
total_transactions.sql
fraud_vs_normal.sql
risk_level_analysis.sql
```
Run these queries directly in Athena

### 8 Run Athena Queries Using Python (Automation)
This project includes a Python script for executing Athena queries programmatically.

Script location:
```
athena/athena_script.py
```
Run the script:
```
python athena/athena_script.py
```
The script will:
- Execute Athena queries
- Fetch query results
- Store results in:
```
s3://fraud-detection-data-lake/athena-results/
```

### Query Results
Athena stores query outputs in:
```
s3://fraud-detection-data-lake/athena-results/
```
These results can be downloaded or used for further analytics

## Results & Insights
Key insights obtained from the analysis:
- Total number of transactions
- Fraud vs normal transaction distribution
- Average fraud transaction amount
- High value fraudulent transactions
- Transaction risk levels

## Author
```
Name: Vilas K R
GitHub: https://github.com/vilas-kr
```




