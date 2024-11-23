N = int(raw_input())
data = raw_input().split(" ")

data = map(int,data)


data = set(data)
data = list(data)
data.sort()
print data[-2]
