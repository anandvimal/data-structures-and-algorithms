n=[-1000000000,1,6,2,45,4,90,98,101,8,9,104,230,34,30,400]

def LISbigger(i,j):
    if j>len(n)-1:
        return 0
    elif n[i]>= n[j]:
        return LISbigger(i,j+1)
    else:
        skip = LISbigger(i,j+1)
        take = 1 + LISbigger(j,j+1)
    
        return max(skip,take)

def LIS(n):
    n[0] = -1000000000
    return LISbigger(0,1)

print(LISbigger(0,1))
print(LIS(n))

