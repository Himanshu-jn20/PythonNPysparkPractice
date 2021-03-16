from pyspark import SparkContext, SparkConf

conf=SparkConf().setMaster('local').setAppName('minTemp')
sc=SparkContext(conf=conf)

def Parser(line):
    LineS=line.split(',')
    year=LineS[1][0:4]
    return(LineS[0],year,LineS[2],float(LineS[3]))


lines=sc.textFile('C:\\Users\\lenovo\\Desktop\\Files\\1800.csv')
linesClean=lines.map(Parser).filter(lambda x:x[2] in ['TMIN'])
res=linesClean.count()
print(res)
#This is avg - linesAvg=linesClean.map(lambda x:(x[0],x[3])).mapValues(lambda x:(x,1)).reduceByKey((lambda x,y:(x[0]+y[0],x[1]+y[1])))
#ll=linesAvg.mapValues(lambda x:x[0]//x[1])
minTemp=linesClean.map(lambda x:(x[0],x[3])).reduceByKey(lambda x,y:min(x,y))
#ll=minTemp.collect()

# ss=ll.count()
# print(ss)

GetResult=minTemp.collect()
for result in GetResult:
    print(result)


