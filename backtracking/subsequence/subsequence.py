def LISbigger(prev: int, sequence ):
    length_of_sequence = len(sequence)
    if length_of_sequence == 0:
        return 0
    elif sequence[0] <= prev :
        return LISbigger(prev, sequence[1:])
    else:
        skip = LISbigger(prev, sequence[1:])
        take = LISbigger(sequence[0], sequence[1:]) +1 
        return max(skip,take)
print( LISbigger(-1,[3,1,4,1,5,9,2,6,5,3,5,8,9]) )


sequence = [3,1,4,1,5,9,2,6,5,3,5,8,9]
def LISbiggerGlobalArray(prev: int, starting_index: int ):
    length_of_sequence = len(sequence)
    if starting_index == length_of_sequence:
        return 0
    elif sequence[prev] >= sequence[starting_index] :
        return LISbiggerGlobalArray(sequence[prev], starting_index+1)
    else:
        skip = LISbiggerGlobalArray(prev, starting_index+1)
        take = LISbiggerGlobalArray(starting_index, starting_index+1) +1 
        return max(skip,take)
print(LISbiggerGlobalArray(0, 1))


# A = [3,1,4,1,5,9,2,6,5,3,5,8,9]
# def LISfirst(i):
#     best = 0
#     for j in range(i+1,n):
#         A[j] > A[i]