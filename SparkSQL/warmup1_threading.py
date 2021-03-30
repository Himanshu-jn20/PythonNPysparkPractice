from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import time
import time
import threading

spark = SparkSession.builder \
    .master("local") \
    .config("spark.sql.autoBroadcastJoinThreshold", -1) \
    .config("spark.executor.memory", "500mb") \
    .appName("Exercise1") \
    .getOrCreate()

prdDf=spark.read.format('parquet').load('/home/hjain/Desktop/work/Files/Exercise/SixSparkEx/products_parquet')
salesDf=spark.read.format('parquet').load('/home/hjain/Desktop/work/Files/Exercise/SixSparkEx/sales_parquet').cache()
sellerDf=spark.read.format('parquet').load('/home/hjain/Desktop/work/Files/Exercise/SixSparkEx/sellers_parquet')
#prdDf.show()

def prd_cnt(df):
    prd=df.count()


def sales_cnt(df):
    sal=df.count()


def seller_cnt(df):
    sell=df.count()

time1=time.time()
#prd = prdDf.count()
#sal = salesDf.count()
#sell = sellerDf.count()
thr1=threading.Thread(target=prd_cnt, args=(prdDf,))
thr2=threading.Thread(target=sales_cnt, args=(salesDf,))
thr3=threading.Thread(target=seller_cnt, args=(sellerDf,))

thr1.start()
thr2.start()
thr3.start()

thr1.start()
thr2.start()
thr3.start()

thr2.join()
top=salesDf.groupBy("product_id").agg(count("*").alias("cnt")).orderBy(col("cnt").desc()).limit(1).show()

thr1.join()
thr3.join()
time_taken=time.time()-time1

print(f'count done {time_taken}')
print(f'product - {prd} , ord - {sal}, sellers - {sell}')
#salesDf.printSchema()

#distinct products
#disDF=salesDf.select("product_id").distinct()
#./disDF.show()

