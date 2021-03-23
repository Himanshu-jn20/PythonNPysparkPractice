from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .master("local") \
    .config("spark.executor.memory","500mb") \
    .appName("union") \
    .getOrCreate()

prdDf=spark.read.parquet('/home/hjain/Desktop/work/Files/Exercise/SixSparkEx/products_parquet')
salesDf=spark.read.format('parquet').load('/home/hjain/Desktop/work/Files/Exercise/SixSparkEx/sales_parquet')

print(prdDf.count())
print(salesDf.count())

df=prdDf.select(col("product_id")).union(salesDf.select(col("product_id"))).distinct() #Distinct is needed because union allowes duplicates like union all
print(df.count())