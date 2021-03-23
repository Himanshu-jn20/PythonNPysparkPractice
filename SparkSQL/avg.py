from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .master("local") \
    .config("spark.executor.memory","500mb") \
    .appName("union") \
    .getOrCreate()

df=spark.read.csv('/home/hjain/Desktop/work/Files/num.txt',sep=' ').toDF("num","xx")
df.show()
df.agg(round(avg(col("num")),2)).show()