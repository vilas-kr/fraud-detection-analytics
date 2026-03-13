import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

transactions = spark.read \
    .option('header', True) \
    .option('inferSchema', True) \
    .csv(args['INPUT_PATH'])
    
transactions = transactions.withColumn(
        'risk_level',
        when(col('amount') < 50, 'Low Risk') \
        .when(col('amount') <= 200, 'Medium Risk') \
        .otherwise('High Risk')
    )
print('Risk level column added successfully')

transactions.write \
    .mode('overwrite') \
    .parquet(args['OUTPUT_PATH'])
print(f'Result dataset stored in {args["OUTPUT_PATH"]}')

job.commit()