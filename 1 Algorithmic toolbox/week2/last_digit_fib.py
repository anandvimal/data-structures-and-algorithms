from math import sqrt

def get_fib(position: int):
    secondlastfib=0
    lastfib=1
    if position ==0:
        return 0
    elif position ==1:
        return 1
    else:
        for i in range(1,position):
            current = (secondlastfib + lastfib) % 10
            secondlastfib = lastfib % 10 
            lastfib = current % 10
            #print(f"{i} : {current}")
    return current

# def fixed_fib(position: int):
#     # phi = 1.61803398874989484820
#     # phi = 1.618033988749895
#     phi = (1 + (5)**(0.5))/2
#     #phi = ((5)**(0.5) - 1)/2
#     phi_power_n = phi ** position
#     neg_phi_power_neg_n = (-phi) ** (-position)
#     root5= 5.0 ** (1.0/2.0)
#     fibonnaci = (phi_power_n - (neg_phi_power_neg_n) )/ root5
#     return fibonnaci

# def nthFib(n):
#     res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
#     # compute the n-th fibonacci number
#     #print(int(res),'is',str(n)+'th fibonacci number')
#     # format and print the number
#     return int(res)

fib_position = input("")
fib_position= int(fib_position)

# long_number = (fixed_fib(fib_position))
# print(int(long_number))

long_number = (get_fib(fib_position))
print(int(long_number))
# long_number = (nthFib(fib_position))
# print(long_number)

