def binary_search(sorted_list: list,lookup_item: int ):
    low = 0
    high = len(sorted_list)-1
    #print(f"looking for {lookup_item}")
    # implementation
    while( low <= high ):
        #print(f"low:{low} high:{high}")
        mid = int((low+high)/2)
        if lookup_item == sorted_list[mid]:
            #print(f"found {sorted_list[mid]}")
            return mid 
        elif lookup_item > sorted_list[mid]:
            low = mid + 1
        elif lookup_item < sorted_list[mid]:
            high = mid - 1
    return -1

def binary_search_wrapper(sorted_list: list, lookup_item: int):
    result_index = binary_search(sorted_list, lookup_item)
    while (result_index > 0 and sorted_list[result_index] == lookup_item):
        if sorted_list[result_index-1] == lookup_item:
            result_index = result_index-1
        else:
            return result_index
    return result_index
    

if __name__ == "__main__":
    number_of_enteries = int(input()) #ignore
    original_list = list(map(int, input().split()))
    number_of_enteries = int(input()) #ignore
    search_list = list(map(int, input().split()))
    result_list = ''
    for search_item in search_list:
        result = binary_search_wrapper(sorted_list = original_list,lookup_item= search_item )
        result_list = result_list + str(result) + ' '
    print(result_list)


'''
binarySearch(arr, x, low, high)
    repeat till low = high
           mid = (low + high)/2
           if (x = arr[mid])
               return mid
          else if (x > arr[mid])
               low = mid + 1
          else
               high = mid – 1
'''