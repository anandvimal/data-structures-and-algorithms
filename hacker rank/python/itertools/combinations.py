from itertools import permutations

word, length = raw_input().split(" ")
length = int(length)

for i in range(1,length+1):
    data = list(permutations(list(word),i))

    neo = []

    for i in data:
        neo.append(list(i))

    neo.sort()

    for i in neo:
        i.sort()

    data2 = []
    for i in neo:
        data2.append("".join(i))

    data2 = set(data2)
    data2 = list(data2)
    data2.sort()
    
    for i in data2:
        print i
