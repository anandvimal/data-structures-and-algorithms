
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
    #print(f"{gcd}")
    product = a*b
    lcm = product/gcd
    print(f"{int(lcm)}")
