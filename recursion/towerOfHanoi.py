
def hanoi(n, src, dst, tmp):
    if n == 0:
        "this is moved!"
    elif n > 0:
        hanoi(n-1, src, tmp, dst)
        print(f"Move disk:{n} from source:{src} to destination:{dst}")
        hanoi(n-1, tmp, dst, src)
    

hanoi(4, "S", "D", "H")