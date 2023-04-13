#from math import sqrt
import math
#from turtle import position

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

def last_digit_sum_fibonacci(position: int):
#def last_digit_sum_fibonacci(position: int, position_start, position_last):
    total_mod_10 =0
    q_total_mod_10 = 0
    r_total_mod_10 = 0
    pisano_period = get_pisano_period(pisano = 10)
    #print(f"pisano_period : {pisano_period}")

    remainder = position % pisano_period
    quotient = math.floor(position / pisano_period)
    #print(f"quotient : {quotient}")
    #print(f"remainder : {remainder}")

    if quotient > 0:
        #calculate 1 round and * by quotient:
        for i in range (0,pisano_period):
            q_total_mod_10 += get_fib(position = i, modulo =  10)
    if remainder > 0: 
        for i in range(0, remainder+1):
            #print("this runs once")
            r_total_mod_10 += get_fib(position = i, modulo = 10)
            
    total_mod_10 = int(q_total_mod_10 * quotient + r_total_mod_10) % 10
    #print(f"total_mod_10 :{total_mod_10}")
    return total_mod_10


if __name__ == "__main__":    
    position_small, position_large = map(int, input().split())
    #position = 3
    total_mod10_small = last_digit_sum_fibonacci(position_small-1) #n-1 because we need Fn+ Fn+1 + .... + Fm
    total_mod10_large = last_digit_sum_fibonacci(position_large)
    #print(f"total_mod10_small : {total_mod10_small}, total_mod10_large : {total_mod10_large} ")
    result = (total_mod10_large - total_mod10_small) 
    if result<0: # if sum till Fn-1 mod 10 > sum Fn..Fm mod 10 (we just need to add 10 to negative to get the correct answer. think on it :p)
        result = 10 + result
    print( (result))

