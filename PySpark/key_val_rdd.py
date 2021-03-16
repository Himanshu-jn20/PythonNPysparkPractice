from pyspark import SparkContext,SparkConf
conf= SparkConf().setMaster("local").setAppName("FriendsByAge")
sc=SparkContext(conf=conf)

def Parser(line):
    sp=line.split(',')
    return(int(sp[2]),int(sp[3]))

lines=sc.textFile("/media/hjain/Windows/Users/lenovo/Desktop/Files/fakefriends.csv")
age_friends=lines.map(Parser)
age_frnd_num=age_friends.mapValues(lambda x:(x,1)).reduceByKey(lambda x,y:(x[0]+y[0],x[1]+y[1]))
avg_age_friends=age_frnd_num.mapValues(lambda x:x[0]//x[1])
GetResult=avg_age_friends.collect()
for result in GetResult:
    print(result)