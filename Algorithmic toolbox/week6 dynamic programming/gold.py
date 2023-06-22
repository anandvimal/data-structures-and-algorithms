#items = [1,4,8]
value = {}

def knapsack(W, items, n):
    for w in range(0,W+1):
        value[w,0] = 0
    for j in range(0,n+1):
        value[0,j]=0
    for i in range(1,n+1):
        for w in range(1,W+1):
            value[w,i] = value[w,i-1]
            wi = items[i-1]
            vi = items[i-1]
            if wi <= w:
                val = value[w-wi,i-1]+vi
                if value[w,i] < val:
                    value[w,i] = val
    return value[W,n]

#print(knapsack(W=10))




if __name__ == "__main__":
    W, x = map(int, input().split())
    items = list(map(int, input().split()))
    n = len(items)
    print(knapsack(W=W, items = items, n=n))