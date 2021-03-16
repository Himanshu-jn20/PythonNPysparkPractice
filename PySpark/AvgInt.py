from pyspark import SparkContext,SparkConf
conf=SparkConf().setMaster('local').setAppName('avg')
sc=SparkContext(conf=conf)

def myAvg(x, y):
    return (x+y)/2.0;


rdd=sc.textFile('/home/hjain/Desktop/work/Files/num.txt')
#rdd1=rdd.map(lambda x:(int(x),1))
#rddx=rdd1.reduce(lambda x,y:x[0]+y[0])
rddx=rdd.map(lambda x:(int(x),1)).reduce(lambda x,y:(x+y)/2)
#rdd2=rddx.collect()
print(rddx)
avg = rdd.map(lambda x:int(x)).reduce(myAvg)
print(avg)
