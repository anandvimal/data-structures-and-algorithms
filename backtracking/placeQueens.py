#Q --> queens position array. [1,2,3,4,5,6,7,8] where each step is position of queen in next row. eg: position of queen at 1st row is 1. 

# def place_queens(Q, r):
#     n = len(Q)
#     print(f"n = {n}")
#     if r==n+1:
#         print(Q)
#         return Q
#     else:
#         for j in range(1,n):
#             print(f"J = {j}")
#             legal = True
#             for i in range(1,r-1):
#                 #print(Q)
#                 print(f"j={j} i={i} Q[i]={Q[i]} r={r}")
#                 if(Q[i] == j) or (Q[i]==j+r-i) or (Q[i]==j-r+i):
#                     legal = False
#             if legal:
#                 Q[r-1] = j
#                 print(Q)
#                 place_queens(Q, r+1)
#                 print(Q)
# Q = [None,None,None,None]
# place_queens(Q=Q,r=1)

def place_queens_py(Q=[None,None,None,None], r=0):
    n=len(Q)
    #print("this starts here")
    if r==n:
        print(Q)
        #input()
    else:
        for j in range(0,n):
            legal = True
            for i in range(0, r+1): #check this limit for r -1 or -2
                #print(f"Q[i]={Q[i]}, j={j}")
                if (Q[i]==j) or (Q[i] == j+r-i) or (Q[i]==j-r+i) :
                    legal = False
                    #print(f"can not add {Q[r]} = {j}")
            if legal:
                Q[r] = j
                #print(Q)
                place_queens_py(Q,r+1)
place_queens_py()