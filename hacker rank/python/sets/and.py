#set intersection operator. 

raw_input()
n = raw_input().split()
n = map(int,n)
n = set(n)

raw_input()
m = raw_input().split()
m = map(int,m)
m = set(m)

print len(n.intersection(m))
