from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc=SparkContext("local[2]","FileStream")
ssc=StreamingContext(sc,5)

lines=ssc.textFileStream("/home/hjain/Desktop")
words = lines.flatMap(lambda x: x.split(" "))
pairs = words.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
pairs.pprint()

ssc.start()
ssc.awaitTermination()
