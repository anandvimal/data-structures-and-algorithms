Edit = {}
#def editDistance(A : str , B: str):
def editDistance(A , B):
    n = len(B)+1
    m= len(A)+1
    for j in range(0,n):
        Edit[0,j]=j
        #Edit.insert([0][j],j)
    for i in range(1,m):
        Edit[i,0] = i
        
        for j in range(1,n):
            insert = Edit[i,j-1]+1
            delete = Edit[i-1,j]+1
            if A[i-1] == B[j-1]:
                rep = Edit[i-1,j-1]
            else:
                rep = Edit[i-1,j-1]+ 1
            Edit[i,j]= min(insert, delete, rep)
            #print(Edit[m-1,n-1])

    #print(Edit)
    return Edit[m-1,n-1]

#result=editDistance("this","that")
#print(f"edit distance for this and that is: {result}")

#result=editDistance("xxxx","that")
#print(f"edit distance for this and that is: {result}")


# https://stackoverflow.com/questions/2460177/edit-distance-in-python/24172422#24172422
# def edit_distance(s1, s2):
#     m=len(s1)+1
#     n=len(s2)+1

#     tbl = {}
#     for i in range(m): tbl[i,0]=i
#     for j in range(n): tbl[0,j]=j
#     for i in range(1, m):
#         for j in range(1, n):
#             cost = 0 if s1[i-1] == s2[j-1] else 1
#             tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

#     print(tbl)
#     #return tbl[i,j]
#     return tbl[n-1,m-1]

# print(edit_distance("Helloworld", "HalloWorld"))
# print(edit_distance("this", "that"))
# print(edit_distance("xxxx", "that"))


if __name__ == "__main__":
    A = str(input()) #ignore
    B = str(input())#money = 10
    result = editDistance(A,B)
    print(result)