# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(raw_input())

store = []

for i in range(0,n):
    data = (raw_input()).split(" ")
    if (data[0] == "insert"):
        store.insert( int(data[1]), int(data[2]) )
        #print store
    elif (data[0]== "print"):
        #print "printing store",
        print store
    elif (data[0] == "remove") :
        store.remove( int(data[1]) )
        #print store
    elif (data[0] == "append") :
        store.append(int(data[1]))
        #print store
    elif (data[0] == "sort"):
        store.sort()
        #print store
    elif (data[0] == "pop"):
        store.pop()
        #print store
    elif data[0] == "reverse" :
        store.reverse()
        #print store
