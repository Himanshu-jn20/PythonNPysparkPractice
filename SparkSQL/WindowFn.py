from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Row,Window
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

salesGpDf=salesDf.groupby(col("product_id"),col("seller_id")).agg(sum("num_pieces_sold").alias("tot_pcs"))
salesGpDf.withColumn("rank",dense_rank().over(Window.partitionBy("product_id").orderBy(col("tot_pcs").desc()))) \
    .where((col("rank")==1) & (col("product_id")==0)).show()