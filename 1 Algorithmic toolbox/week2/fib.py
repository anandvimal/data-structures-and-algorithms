
def get_fib(position: int):
    secondlastfib=0
    lastfib=1
    if position ==0:
        return 0
    elif position ==1:
        return 1
    else:
        for i in range(1,position):
            current = secondlastfib + lastfib
            secondlastfib = lastfib
            lastfib = current
            #print(f"{i} : {current}")
    return current

fib_position = input("")
fib_position= int(fib_position)

print(get_fib(fib_position))