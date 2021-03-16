from pyspark import SparkContext,SparkConf
conf=SparkConf().setMaster('local').setAppName('word_count')
sc=SparkContext(conf=conf)

import re,collections

def clean(text):
    return re.compile(r'\W+',re.UNICODE).split(text.lower())

inputt=sc.textFile('/media/hjain/Windows/Users/lenovo/Desktop/Files/Book.txt')
#words=input.flatMap(lambda x:x.split())
words=inputt.flatMap(clean)
#wordsCnt=words.countByValue()
#print(sorted(wordsCnt.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))

#sort using RDD
wordsCnt=words.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
wordsCntSort_1=wordsCnt.map(lambda x: (x[1],x[0])).sortByKey()

wordsCntSort=wordsCntSort_1.collect()

#for i,v in sorted(wordsCnt.items(), key = lambda kv:(kv[1], kv[0]),reverse=True):
for x in wordsCntSort:
        print(x[1],x[0])