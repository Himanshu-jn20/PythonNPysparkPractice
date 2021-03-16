from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularMovies")
sc = SparkContext(conf = conf)

def MovieNames():
    movie_Names={}
    with open('C:\\Users\\lenovo\\Desktop\\Files\\ml-100k\\u.item', 'r') as f:
        for ln in f:
            line=ln.strip()
            lval=line.split('|')
            movie_Names[int(lval[0])]=lval[1]
    return movie_Names

nameDict = sc.broadcast(MovieNames())

lines = sc.textFile("C:\\Users\\lenovo\\Desktop\\Files\\ml-100k\\u.data")
movies = lines.map(lambda x: (int(x.split()[1]), 1))
movieCounts = movies.reduceByKey(lambda x, y: x + y)

flipped = movieCounts.map(lambda countMovie : (nameDict.value[countMovie[1]], countMovie[0]))
sortedMovies = flipped.sortByKey()

results = sortedMovies.collect()

for result in results:
    print(result)

