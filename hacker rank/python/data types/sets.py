# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(raw_input())
list1 = raw_input().split(" ")
list1 = map(int, list1)

N = int(raw_input())
list2 = raw_input().split(" ")
list2 = map(int, list2)

s1 = set(list1)
s2 = set(list2)

#print s1
#print s2

all_s =  s1.union(s2)
common_s = list( s1.intersection(s2) )

for i in common_s:
    all_s.discard(i)

all_s = list(all_s)

all_s.sort()
#all_s.discard(common_s)
for i in all_s:
    print i
