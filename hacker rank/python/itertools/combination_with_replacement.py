# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

word, n =  raw_input().split()
n = int(n)

result = list(combinations_with_replacement(word,n))
neo = []

for i in result:
    i = list(i)
    i.sort()
    neo.append("".join(i))

neo.sort()

for i in neo:
    print i
