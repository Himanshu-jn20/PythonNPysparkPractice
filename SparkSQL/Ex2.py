from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Row
from pyspark.sql.types import IntegerType
import time

spark = SparkSession.builder \
    .master("local") \
    .config("spark.sql.autoBroadcastJoinThreshold", -1) \
    .config("spark.executor.memory", "2g") \
    .appName("Exercise1") \
    .getOrCreate()

prdDf=spark.read.format('parquet').load('/home/hjain/Desktop/work/Files/Exercise/SixSparkEx/products_parquet')
salesDf=spark.read.format('parquet').load('/home/hjain/Desktop/work/Files/Exercise/SixSparkEx/sales_parquet')
sellerDf=spark.read.format('parquet').load('/home/hjain/Desktop/work/Files/Exercise/SixSparkEx/sellers_parquet')

salesDf.groupby("seller_id").agg(avg("num_pieces_sold").alias("avgPcs")) \
    .join(broadcast(sellerDf),salesDf["seller_id"]==sellerDf["seller_id"],"inner") \
    .withColumn("Perc",col("avgPcs")/sellerDf["daily_target"]).show()
