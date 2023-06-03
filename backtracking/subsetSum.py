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
        

#lets test the subset_sum:
test_bank = {
    5:[],
    -1:[1,2,3,4],
    0:[],
    9:[5,4,3,2,1,6,66],
    9:[5,1,5,7,4,11,635]
    }

for key in test_bank:
    result = subset_sum(X=test_bank[key], i=len(test_bank[key]), T=key)
    print(f"total:{key}, set:{test_bank[key]}, is_subset:{result}")
    