import boto3
import time
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

DATABASE = 'fraud_detection_db'
OUTPUT = 's3://vilas-fraud-detection-datalake/query_results/'

query = '''
SELECT class, COUNT(*) AS total_transaction
FROM fraud_detection_db.creditcard_transactions
GROUP BY class;
'''

athena = boto3.client('athena')

response = athena.start_query_execution(
    QueryString=query,
    QueryExecutionContext={'Database': DATABASE},
    ResultConfiguration={'OutputLocation': OUTPUT}
)
logging.info(f'Query started with execution ID: {response["QueryExecutionId"]}')


query_id = response['QueryExecutionId']

while True:
    status = athena.get_query_execution(QueryExecutionId=query_id)
    state = status['QueryExecution']['Status']['State']

    if state in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
        break
    time.sleep(2)
    logging.info(f'Query status: {state}')

if state == 'SUCCEEDED':
    logging.info('Query succeeded.')
    results = athena.get_query_results(QueryExecutionId=query_id)
    for row in results['ResultSet']['Rows']:
        [print(f'{col.get('VarCharValue', '')} \t', end='') for col in row['Data']]
        print()


