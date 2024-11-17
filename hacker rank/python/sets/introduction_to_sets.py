# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
data = raw_input().split(" ")
data = map(int,data)

data = set(data)
data = list(data)

number_of_plants = len(data)
sum = 0.0
for i in data:
    sum = sum+i

print (sum/number_of_plants)
