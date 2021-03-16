from pyspark import SparkConf, SparkContext
import time

def loadMovieNames():
    movieNames = {}
    with open("C:\\Users\\lenovo\\Desktop\\Files\\ml-100k\\u.item") as f:
        for line in f:
            fields = line.split('|')
            time.sleep(100)
            movieNames[int(fields[0])] = fields[1]
    return movieNames

conf = SparkConf().setMaster("local").setAppName("PopularMovies")
sc = SparkContext(conf = conf)

nameDict = sc.broadcast(loadMovieNames())

lines = sc.textFile("C:\\Users\\lenovo\\Desktop\\Files\\ml-100k\\u.data")
movies = lines.map(lambda x: (int(x.split()[1]), 1))
movieCounts = movies.reduceByKey(lambda x, y: x + y)

flipped = movieCounts.map( lambda x : (x[1], x[0]))
sortedMovies = flipped.sortByKey()

sortedMoviesWithNames = sortedMovies.map(lambda countMovie : (nameDict.value[countMovie[1]], countMovie[0]))

time.sleep(100)

results = sortedMoviesWithNames.collect()

for result in results:
    print (result)
