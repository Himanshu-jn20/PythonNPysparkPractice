from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)

lines = ssc.socketTextStream("localhost",9999)
words = lines.flatMap(lambda x: x.split(" "))
pairs = words.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
pairs.pprint()

ssc.start()
ssc.awaitTermination()

# port opening and data writing can be do by running the command "nc -lk 9999" on terminal.