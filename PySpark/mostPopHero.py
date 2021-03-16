from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("mostPopularHero")
sc = SparkContext(conf=conf)


def Parser(line):
    spl = line.split('\"')
    return (int(spl[0]), spl[1])


def countCoOcc(line):
    spl = line.split()
    return (int(spl[0]), len(spl)-1)


names = sc.textFile("C:\\Users\\lenovo\\Desktop\\Files\\Marvel_Names.txt")
namesRdd = names.map(Parser)

lines = sc.textFile("C:\\Users\\lenovo\\Desktop\\Files\\Marvel_Graph.txt")
linesRdd = lines.map(countCoOcc).reduceByKey(lambda x,y:x+y)
flipped = linesRdd.map(lambda xy: (xy[1], xy[0]))
mostPop = flipped.max()

print(mostPop[1])
aa=namesRdd.take(5)
print(aa)

mostPopname = namesRdd.lookup(mostPop[1])[0]
print(f'mostPopname - {mostPopname} with {mostPop[0]} occurences')





