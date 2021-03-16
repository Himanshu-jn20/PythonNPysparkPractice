from pyspark.sql import SparkSession,Row,functions

def loadMovieNames():
    movieNames = {}
    with open("C:\\Users\\lenovo\\Desktop\\Files\\ml-100k\\u.item") as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
    return movieNames

spark=SparkSession.builder.config("spark.sql.warehouse.dir","C:\\sparkcourse").appName("PopMovs").getOrCreate()

nameDict = loadMovieNames()

lines = spark.sparkContext.textFile("C:\\Users\\lenovo\\Desktop\\Files\\ml-100k\\u.data")
movies = lines.map(lambda x: Row(movieId=int(x.split()[1])))
df = spark.createDataFrame(movies)
topMov = df.groupBy("movieId").count().orderBy("count",ascending = False).cache()
topMov.show()


