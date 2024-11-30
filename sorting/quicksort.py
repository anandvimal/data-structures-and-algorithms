A = [6,5,3,4,65,7,23,16]

def partition(A, p, r):
    x = A[r] # pivot ?
    i = p -1 # ?
    for j in range(p, r):
        if A[j] <= x:
            i = i+1 # left pointer increases if its smaller than pivot.
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    print(f"pivot is {A[i+1]} and array is {A}")
    return i+1 #pivot

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p , r) #q becomes pivot
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

print(f"unsorted array : {A}")
quicksort(A,p=0, r=len(A)-1)
print(f"sorted array : {A}")