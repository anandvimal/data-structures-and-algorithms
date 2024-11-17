N = int(raw_input())

data = raw_input().split(" ")

data = map(int, data)
data = set(data)

N = int(raw_input())
c=""
n=""

for i in range(0,N):
    line = raw_input()
    if line == "pop":
        data.pop()
        #print data
    else:
        line = line.split(" ")
        #print line
        c = line[0]
        n = int(line[1])
        #print c,n

    if c == "remove":
        if n in data:
            data.remove(n)
            #print "remove",data
        #print data
    elif c == "discard":
        data.discard(n)
        #print data

sum = 0

#print "sum",data
for i in data:
    sum = sum+ i

print sum
