# def gcd(a, b):
#     smaller_number = min(a,b)
#     larger_number = max(a,b)

#     if smaller_number%2==0 and larger_number%2==0:
#         for divisor in range (smaller_number,0, -1):
#             if smaller_number%divisor==0:
#                 if larger_number%divisor==0:
#                     gcd = divisor
#                     return gcd
#     elif smaller_number%2 != 0:
#         for divisor in range (smaller_number,0, -2):
#             if smaller_number%divisor==0:
#                 if larger_number%divisor==0:
#                     gcd = divisor
#                     return gcd
#     else:
#         for divisor in range (smaller_number-1,0, -2):
#             if smaller_number%divisor==0:
#                 if larger_number%divisor==0:
#                     gcd = divisor
#                     return gcd
#     return 1

# def gcd1(a,b):
#     current_gcd = 1
#     for divisor in range(1, min(a,b)+1):
#         if a%divisor==0 and b%divisor==0:
#             current_gcd = divisor
#     return current_gcd

# def lcm(a,b):
#     minimum = min(a,b)
#     maximum = max(a,b)
#     product = a*b
#     max_list = []
#     counter = 1 #start counter at 1
#     while ( (x:=minimum*counter) <= product):
#         max_list.append(maximum*counter)
#         if x in max_list:
#             print(f"lcm: {x}")
#             return x # lcm
#         print(f"x:{x} max_list:{max_list}")
#         counter+=1
#     return 0


# def gcd_by_lcm(a,b):
#     product = a*b 
#     lcm_value = lcm(a,b)
#     gcd = (product* 1.0)/(lcm_value*1.0)
#     return gcd

def gcd_eucledian(a,b):
    if a==0:
        #print(f"return b:{b}")
        return b
    if b==0:
        #print(f"return a:{a}")
        return a
    #print(f"a:{a} b:{b}")
    holder = a%b
    a=b
    b=holder
    #print(f"a:{a} b:{b} holder:{holder}")
    return gcd_eucledian(a,b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    #print(lcm(a,b))
    if a >= b:
        pass
    else:
        holder = a
        a = b 
        b = holder        
    gcd=gcd_eucledian(a,b)
    print(f"{gcd}")