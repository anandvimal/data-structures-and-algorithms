N = raw_input().split(" ")
N = map(int,N)

M = raw_input().split(" ")
M = map(int, M)

data = []
for i in N:
    for j in M:
         data.append( (i,j) )

for i in data:
    print i,
