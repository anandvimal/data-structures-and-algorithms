import sys

N = int(raw_input())
T = raw_input().split(" ")
#print T

data = []
for i in T:
    data.append( int(i) )

tup = tuple(data)

print hash(tup)
