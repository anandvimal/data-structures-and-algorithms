import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

x=0
sum1 = 0
sum2 = 0
for i in a:

    d1 = i[x]
    d2 = i[len(i)-1-x]

    #print d1
    #print d2
    #print " "
    sum1 = d1 + sum1
    sum2 = d2 + sum2
    x+=1

#print sum1
#print sum2
#print " "

print abs(sum1-sum2)
