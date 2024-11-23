# Enter your code here. Read input from STDIN. Print output to STDOUT

line = raw_input()
#line = line.lower()
#print line

sub = raw_input()
#sub = sub.lower()
#print sub

l = line.find(sub)
count = 0

while( l >= 0):
    count += 1
    line=line[l+1:]
    l = line.find(sub)

print count
