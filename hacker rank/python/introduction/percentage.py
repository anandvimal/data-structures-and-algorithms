N = int(raw_input())

data = []

for i in range(0,N):
    student = raw_input().split(" ")
    data.append( [ student[0] , float(student[1]), float(student[2]), float(student[3]) ] )

percentage = []

for i in data:
    p = (i[1]+i[2]+i[3])/3.0
    percentage.append([i[0],p ])

query = raw_input()

for i in percentage:
    if i[0] == query:
        print ("%.2f" % i[1])
