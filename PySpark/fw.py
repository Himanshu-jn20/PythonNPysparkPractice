from pyspark import SparkContext,SparkConf
conf=SparkConf().setMaster('local').setAppName('avg')
sc=SparkContext(conf=conf)

def ReadF(text):
	col1=text[0:3]
	col2=text[3:6]
	col3=text[6:9]
	return(col1,col2,col3)

rdd=sc.textFile('/home/hjain/Desktop/work/Files/fw.txt')
rdd1=rdd.map(ReadF)
rdd2=rdd1.collect()

print(rdd2)
