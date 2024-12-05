def max_heapify(A, i):
    left = (2*i)
    right = (2*i)+1
    largest = i

    if left <= len(A) and A[left] > A[largest]:
        largest = left

    if right <= len(A) and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,largest)