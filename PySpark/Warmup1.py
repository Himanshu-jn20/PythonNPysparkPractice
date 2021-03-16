from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .config("spark.sql.autoBroadcastJoinThreshold", -1) \
    .config("spark.executor.memory", "500mb") \
    .appName("Exercise1") \
    .getOrCreate()

dfSell=spark.read.parquet("C:\\Users\\lenovo\\Downloads\\DatasetToCompleteTheSixSparkExercises\\sellers_parquet")
dfSales=spark.read.parquet("C:\\Users\\lenovo\\Downloads\\DatasetToCompleteTheSixSparkExercises\\sales_parquet")
dfPrd=spark.read.parquet("C:\\Users\\lenovo\\Downloads\\DatasetToCompleteTheSixSparkExercises\\products_parquet")

#dfSales.show()
df2=dfSales.groupBy("product_id").count().orderBy("count",ascending = False)
df2.show()