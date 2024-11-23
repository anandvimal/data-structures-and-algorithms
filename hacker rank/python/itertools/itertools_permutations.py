from itertools import permutations

word, length = raw_input().split(" ")
length = int(length)

data = list(permutations(list(word),length))

neo = []

for i in data:
    neo.append("".join(list(i)))

neo.sort()

for i in neo:
    print i
