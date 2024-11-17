N = int(raw_input())
marks = []
data = []
for i in range(N):
    name = raw_input()
    mark = float(raw_input())
    data.append([name,mark])
    marks.append(mark)

#print data

marks = set(marks)
marks = list(marks)
marks.sort()

sec_mark = marks[1]

result = []
for i in data:
    if sec_mark == i[1]:
        result.append(i[0])

result.sort()

for i in result:
    print i 
