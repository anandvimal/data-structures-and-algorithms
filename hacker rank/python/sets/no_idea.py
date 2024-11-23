# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = raw_input().split()
N = int(N)
M = int(M)

n = raw_input().split()
n = map(int, n)
#n = set(n)

m = raw_input().split()
m = map(int, m)
m = set(m)

c = raw_input().split()
c = map(int, c)
c = set(c)

happy = 0
for i in n:
    if i in m:
        happy += 1
    if i in c:
        happy -= 1

print happy
