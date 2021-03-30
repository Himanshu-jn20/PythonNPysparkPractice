from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import time

spark = SparkSession.builder \
    .master("local") \
    .config("spark.sql.autoBroadcastJoinThreshold", -1) \
    .config("spark.executor.memory", "500mb") \
    .appName("Exercise1") \
    .getOrCreate()

prdDf=spark.read.format('parquet').load('/home/hjain/Desktop/work/Files/Exercise/SixSparkEx/products_parquet')
salesDf=spark.read.format('parquet').load('/home/hjain/Desktop/work/Files/Exercise/SixSparkEx/sales_parquet')
sellerDf=spark.read.format('parquet').load('/home/hjain/Desktop/work/Files/Exercise/SixSparkEx/sellers_parquet')
#prdDf.show()

time1=time.time()
prd=prdDf.count()
sal=salesDf.count()
sell=sellerDf.count()

time_taken=time.time()-time1
print(f'count done {time_taken}')
print(f'product -{prd} , ord -{sal}, sellers -{sell}')
#salesDf.printSchema()

#distinct products
disDF=salesDf.select("product_id").distinct()
disDF.show()

salesDf.groupBy("product_id").agg(count("*").alias("cnt")).orderBy(col("cnt").desc()).limit(1).show()