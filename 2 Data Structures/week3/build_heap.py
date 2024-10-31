# python3
#data = [5,4,3,2,1]
data = [1,2,3,4,5]
size = len(data)-1
swaps = []

def parent(i):
    return int(i/2)

def leftChild(i):
    return (2*i)

def rightChild(i):
    return ((2*i)+1)

def swap(x, y):
    temp = x 
    x = y 
    y = temp

def siftDown(i):
    print(f"index i = {i}")
    maxindex = i
    l = leftChild(i)
    print(f"l = {l}")
    if l <= size and data[l] < data[maxindex]:
        maxindex = l
    r = rightChild(i)
    print(f"r = {r}")
    print(f"data[maxindex] = {data[maxindex]}")
    
    if r <= size and data[r] < data[maxindex]:
        maxindex = r
        print(f"data[r] = {data[r]}")
    if i != maxindex: 
        #swap(data[i], data[maxindex])
        #print(f"swap values: {data[i]} with {data[maxindex]}")
        print(f"swap index: {i} with {maxindex}")
        print(f"swap item {data[i]} with {data[maxindex]}")
        print(f"data before swap: {data}")
        temp = data[i]
        data[i] = data[maxindex]
        data[maxindex] = temp
        print(f"data after swap: {data}")
        siftDown(maxindex)

def BuildHeap(data):
    print(f"data = {data}")
    print(f"size = {size}")
    print(f"size half = {int(size/2)}")
    for i in range(int(size/2), 0, -1):
        siftDown(i)
    print(f"data in the end: {data}")

BuildHeap(data=data)