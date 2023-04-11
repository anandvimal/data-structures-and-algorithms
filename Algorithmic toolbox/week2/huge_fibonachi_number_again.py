from math import sqrt

def get_fib(position: int, modulo: int):
    secondlastfib=0
    lastfib=1
    if position ==0:
        return 0
    elif position ==1:
        return 1
    else:
        for i in range(1,position):
            current = (secondlastfib + lastfib) % modulo
            secondlastfib = lastfib % modulo 
            lastfib = current % modulo
            #print(f"{i} : {current}")
    return current



# def n_fib_mod_m(position: int, modulo: int):
# #def nthFib(n):
#     n = position
#     res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5)) % modulo
#     # compute the n-th fibonacci number
#     print(int(res),'is',str(n)+'th fibonacci number')
#     # format and print the number
#     #result = res % modulo
#     result = res
#     print(result)     
#     pass


'''
references: 
https://medium.com/competitive/huge-fibonacci-number-modulo-m-6b4926a5c836#.8n3hmh3el
https://en.wikipedia.org/wiki/Pisano_period 

if n is too large. we cant really compute n. there is formula to compute n with large numbers at O(1) but it fails.
now since N is large but F(n) % m has repeating sequence. 
if we get the size of repeating sequence say p. we can just do F(n%p) % m

now how to find size of p. (hint from blogs: it always start with 01 and is a repeating sequence)
start calculating fibonacci numbers from 0 1 1 ... and do modulo m for each occurence and keep checking when you get 0 1 (have to ignore the first occurence) and stop when you do find one. 
'''

def get_pisano_period(pisano: int):

    secondlastfib=0
    lastfib=1
    if pisano <1:
        raise("not right data. need atleast 1 or greater number for pisano number calculation")
    if pisano ==1:
        return 1
    elif pisano ==2:
        return  3
    else:
        counter_pisano_size = 0
        pissano_period_incomplete = True
        while(pissano_period_incomplete):
            counter_pisano_size += 1
            current = (secondlastfib + lastfib) % pisano
            secondlastfib = lastfib % pisano
            lastfib = current % pisano
            #print(f"{secondlastfib} {lastfib} {current}")
            if lastfib == 1 and secondlastfib == 0:
                pissano_period_incomplete = False # breaks the loop and we return the pisano
            #print(f"{i} : {current}")
    return counter_pisano_size

if __name__ == "__main__":
    position, modulo = map(int, input().split())
    #fib_number_remainder = get_fib(position, modulo)
    #fib_number_remainder = n_fib_mod_m(position, modulo)
    #print(fib_number_remainder)

    
    pisano_peroid = get_pisano_period(modulo)
    new_fib_position = position % pisano_peroid
    result = get_fib(new_fib_position, modulo)
    print(result)