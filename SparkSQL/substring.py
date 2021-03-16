from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .master("local") \
    .config("spark.sql.autoBroadcastJoinThreshold", -1) \
    .config("spark.executor.memory", "500mb") \
    .appName("substr") \
    .getOrCreate()

df=spark.read.csv('/home/hjain/Desktop/work/Files/substr.txt',).toDF("raw")
#df.printSchema()
df=df.withColumn("Name",substring(col("raw"),1,3)) \
    .withColumn("ID",substring(col("raw"),4,3)) \
    .withColumn("Num",substring(col("raw"),7,3)) \
    .withColumn("Split",split(col("raw"),[0-9])) \
    .drop(col("raw"))

df.show()
#df.withColumn("Num2",when(col("Num")=='',None).otherwise(col("Num"))) \
#    .where(col("Num2").isNull()).show()

#df.repartition(2).write.format("com.databricks.spark.csv").option("header","true").option("quote",'"').mode("overwrite").save('/home/hjain/Desktop/work/Files/substr_out')