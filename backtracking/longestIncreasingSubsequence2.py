n=[-1000000000,1,6,2,45,4,90,98,101,8,9,104,230,34,30,400]



# def LISfirst(i):
#     best = 0
#     for j in range(i+1,len(n)):
#         if n[i]<n[j]:
#             best = max(best, LISfirst(j))
#     return best + 1

def LISfirst(i):
    best = 0
    for j in range(i+1,len(n)):
        if n[i]<n[j]:
            best = max(best,1+ LISfirst(j))
    return best 

def LIS(n):
    #n[0] = -1000000000
    return LISfirst(0) 

print(LIS(n))
print(LISfirst(0))