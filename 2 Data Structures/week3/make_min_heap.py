#week3 assignment question1 working solution
def parent(i):
    return int((i-1)//2)

def leftChild(i):
    return (2*i)+1

def rightChild(i):
    return (2*i)+2

def swap(x, y):
    temp = x 
    x = y 
    y = temp

def siftDown(i):
    global size
    global H
    maxIndex = i
    l = leftChild(i)
    #print(f"leftchild: {l}")
    if l<= size and H[l] < H[maxIndex]:
        #print(f"leftchild: {l} -> {H[l]}")
        maxIndex = l
    r = rightChild(i)
    if r <= size and H[r] < H[maxIndex]:
        maxIndex = r
    if i != maxIndex:
        swap_string  = f"{i} {maxIndex}"
        swap_list.append(swap_string)
        #print(swap_string)
        #swap(H[i], H[maxIndex])
        H[i], H[maxIndex] = H[maxIndex], H[i]
        siftDown(maxIndex)

def buildHeap(H):
    size = len(H)-1
    #print(f"size : {size} and last item is {H[size]}")
    for i in range((size+1)//2, -1, -1):
        siftDown(i)


swap_list = []
no_of_items = int(input())
size = no_of_items-1
H = list(map(int, input().split()))
#print(f"H : {H}")
buildHeap(H)
print(f"{len(swap_list)}")
for swap_squence in swap_list:
    print(swap_squence)
#print(f"H: {H}")
#priority_list = input().strip().split(' ')
    