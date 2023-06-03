#array is X, sum/Total is T
def subset_sum(X,i,T):
    if T==0:
        return True
    elif T<0 or i ==0:
        return False
    else:
        x = X[len(X)-1] #last element in the list to test
        #print(f"x={x}")
        with_x = subset_sum(X, i-1, T-X[i-1])
        without_x = subset_sum(X, i-1, T)
        return with_x or without_x
        #return with_x

y = []
#array is X, sum/Total is T
def subset_sum_output(X,i,T):
    if T==0:
        return True
    elif T<0 or i ==0:
        return None
    else:
        Y = subset_sum_output(X, i-1, T)
        if Y != None :
            return Y
        Y = subset_sum_output(X, i-1, T-X[i-1])
        if Y != None:
            return [Y,X[i-1]]



#lets test the subset_sum:
test_bank = {
    5:[],
    -1:[1,2,3,4],
    0:[],
    10:[5,4,3,2,1,6,66],
    9:[5,1,5,7,4,11,635],
    150:[10,234,34,532,234,1,4,5,2,4,52,234,432,22,22,44,55,66,77,88,33,22,65,25]
    }

for key in test_bank:
    result= subset_sum_output(X=test_bank[key], i=len(test_bank[key]), T=key)
    print(f"testing key:{key} set:{test_bank[key]}")
    print(f"total:{key}, set:{test_bank[key]}, is_subset:{result}")
    print()
    