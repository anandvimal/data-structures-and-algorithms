#Uses python3
import sys
import math

input = sys.stdin.read()
data = list(map(int, input.split()))
n = data[0]
x = data[1::2]
y = data[2::2]

parent = []
rank = []

#disjoin sets:
parent = [i for i in range(n)]
rank = [0 for _ in range(n)]
#print(f"parent: {parent}")
#print(f"rank: {rank}")

def minimum_distance(x, y):
    # x[0] = x[0] * 1.0
    # x[1] = x[1] * 1.0
    # y[0] = y[0] * 1.0
    # y[1] = y[1] * 1.0
    result = 0.
    #write your code here
    # calculate square root of (x2-x1)^2 + (y2-y1)^2
    result = math.sqrt(((x[0]*1.0)-(y[0]*1.0))**2 + ((x[1]*1.0)-(y[1]*1.0))**2)

    return result


# # disjoin sets:
# parent = [i for i in range(n+1)]
# rank = [0 for _ in range(n+1)]
# print(f"parent: {parent}")
# print(f"rank: {rank}")
def make_set(i):
    parent[i] = i
    rank[i] = 0

def find(i):
    # print(f"i:{i} parent:{parent}")
    # while i != parent[i]:
    #     i = parent[i]
    #     return i
    return parent[i]
    
def union(i,j):
    i_id = find(i)
    j_id = find(j)
    if i_id == j_id:
        return 
    minimum = min(i_id, j_id)
    for i in range(n):
        if parent[i] in [i_id, j_id]:
            parent[i] = minimum


if __name__ == '__main__':
    #print("{0:.9f}".format(minimum_distance(x, y)))
    #print("input: ", input)
    #print("data: ", data)
    #print("n: ", n)
    #print("x: ", x)
    #print("y: ", y)

    # #disjoin sets:
    # parent = [i for i in range(n)]
    # rank = [0 for _ in range(n)]
    # print(f"parent: {parent}")
    # print(f"rank: {rank}")

    points = []
    for i in range(n):
        points.append((x[i],y[i]))  

    for vertex in range(0,n):
        make_set(vertex)

    #print(f"parent: {parent}")
    #print(f"rank: {rank}")

    X = set() # empty set
    distances = {}
    for i in range(n):
        for j in range(n):
            if i != j and ((i,j) not in  distances and (j,i) not in distances):   
                distances[(i,j)] = minimum_distance(points[i], points[j])
                #print(f"distances: {distances}")
    # sort the distances
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    #print(f"sorted_distances: {sorted_distances}")
    #print(f"distances: {distances}")
    #print(f"points: {points}")
    # calculate edges

    #for edge in sorted_distances:
        #print(f"edge: {edge}")

    total_distance = 0
    for edge in sorted_distances:
        u = edge[0][0]
        v = edge[0][1]
        #print(f"u: {u} v: {v}")
        #print(f"find(u): {find(u)} find(v): {find(v)}")
        if find(u) != find(v):
            X.add(edge)
            #print(f"X: {X}")
            total_distance += edge[1]
            union(u,v)
    #print(f"X: {X}")
    #print(f"total_distance: {total_distance}")
    total_distance = round(total_distance, 9)
    print(total_distance)


