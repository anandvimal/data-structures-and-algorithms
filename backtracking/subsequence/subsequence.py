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