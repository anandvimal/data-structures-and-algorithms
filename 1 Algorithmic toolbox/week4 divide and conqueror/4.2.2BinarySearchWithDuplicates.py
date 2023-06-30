from math import floor


def binary_search(sorted_list: list,lookup_item: int ):
    low = 0
    high = len(sorted_list)
    #print(f"looking for {lookup_item}")
    # implementation
    while( low < high ):
        #print(f"low:{low} high:{high}")
        mid = int(floor((low+high)/2))
        if sorted_list[mid] < lookup_item :
            low = mid + 1
        else:
            high = mid
    if low < 0 or low > len(sorted_list)-1:
        return -1
    elif sorted_list[low] == lookup_item:
        return low
    else:
        low = -1
        #return -1
    return low

def binary_search_wrapper(sorted_list: list, lookup_item: int):
    result_index = binary_search(sorted_list, lookup_item)
    return result_index
    

if __name__ == "__main__":
    number_of_enteries = int(input()) #ignore
    original_list = list(map(int, input().split()))
    number_of_enteries = int(input()) #ignore
    search_list = list(map(int, input().split()))
    result_list = ''
    for search_item in search_list:
        result = binary_search(sorted_list = original_list,lookup_item= search_item )
        result_list = result_list + str(result) + ' '
    print(result_list)


'''
function binary_search_leftmost(A, n, T):
    L := 0
    R := n
    while L < R:
        m := floor((L + R) / 2)
        if A[m] < T:
            L := m + 1
        else:
            R := m
    return L
'''