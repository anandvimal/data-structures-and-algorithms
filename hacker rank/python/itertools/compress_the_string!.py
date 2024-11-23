from itertools import combinations

word, n = raw_input().split()
n = int(n)

neo = []

for i in range(1,n+1):
    neo.append( list(combinations(word,i)))


r = []
for i in neo:
    for j in i:
        r.append( "".join( list(j) ) )

    r.sort()

    for k in r:
        print k
    r = []
