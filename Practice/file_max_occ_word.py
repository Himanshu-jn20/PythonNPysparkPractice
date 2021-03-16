import collections as c

word_stats={}
word_stats2={}
with open("/media/hjain/Windows/Users/lenovo/Desktop/Files/poems.txt","r") as f:

    #for line in f:
    word_split = f.read().split( )
    #        print(word_split)
    for word in word_split:
        # print(word)
        if word in word_stats:
            word_stats[word] = word_stats[word] + 1
        else:
            # print('yes')
            word_stats[word] = 1

#print(list(word_stats.items()))
print(sorted(word_stats.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)[0][0])
ord_d = c.OrderedDict(sorted(word_stats.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))
print(ord_d)

