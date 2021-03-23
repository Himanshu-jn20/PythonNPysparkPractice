from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Row
from pyspark.sql.types import IntegerType
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

t1=time.time()

#below will take time because of data skewness
#salesDf.join(prdDf,salesDf["product_id"]==prdDf["product_id"],"inner").agg(avg(prdDf["price"]*salesDf["num_pieces_sold"]).alias("avg")).show()

res=salesDf.select("product_id").groupby("product_id").agg(count("*").alias("cnt")).sort(col("cnt").desc()).limit(100).collect()
print(type(res))
REPLICATION_FACTOR = 101
l = []
replicated_products = []
for r in res:
    #print(type(r))
    replicated_products.append(r["product_id"])
    for rep in range(REPLICATION_FACTOR):
        l.append((r["product_id"],rep))

rdd = spark.sparkContext.parallelize(l)
rdd=rdd.map(lambda x:Row(product_id=x[0],rep=int(x[1])))
replicated_df=spark.createDataFrame(rdd)

replicated_df=replicated_df.withColumnRenamed("product_id","product_id_")
prdDf=prdDf.join(broadcast(replicated_df),prdDf["product_id"]==replicated_df["product_id_"],"left"). \
      withColumn("new_key",when(replicated_df["rep"].isNotNull(),concat(prdDf["product_id"],lit("-"),replicated_df["rep"])). \
      otherwise(prdDf["product_id"]))

salesDf=salesDf.withColumn("new_key",when(salesDf["product_id"].isin(replicated_products),concat(salesDf["product_id"],lit("-"),(round(rand(),2)*100).cast(IntegerType()))).otherwise(salesDf["product_id"]))
#salesDf.show()


salesDf.join(prdDf,salesDf["new_key"]==prdDf["new_key"],"inner").agg(avg(prdDf["price"]*salesDf["num_pieces_sold"]).alias("avg")).show()

prdDf=prdDf.withColumnRenamed("product_id","product_id_prd").withColumnRenamed("new_key","new_key_")
joindF=salesDf.join(prdDf,salesDf["new_key"]==prdDf["new_key_"],"inner")
print(joindF.columns)