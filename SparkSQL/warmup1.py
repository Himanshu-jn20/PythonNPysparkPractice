from pyspark.sql import SparkSession
from pyspark.sql.functions import *


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

prd=prdDf.count()
sal=salesDf.count()
sell=sellerDf.count()

print(f'product -{prd} , ord -{sal}, sellers -{sell}')
#salesDf.printSchema()

#distinct products
disDF=salesDf.select("product_id").distinct()
disDF.show()

salesDf.groupBy("product_id").agg(count("*").alias("cnt")).orderBy(col("cnt").desc()).limit(1).show()