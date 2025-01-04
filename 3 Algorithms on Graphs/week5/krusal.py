import math
infinity = math.inf
#negative_infinity = -math.inf

graph_details = list(map(int, input().split())) 
n = graph_details[0] # total vertices
m = graph_details[1] # total edges

#lets make a adj_list
adj_list = {}
edges = []

#keep tracks for visited nodes
#visited = {}
distance = {}
previous = {}

#fill adj_list with all vertices
for vertex in range(1,n+1):
    adj_list[vertex] = [] 
    distance[vertex] = infinity
    previous[vertex] = None

#populate adj list
for i in range(0,m):
    edge = list(map(int, input().split()))
    node_l = edge[0]
    node_r = edge[1]
    weight = edge[2]
    adj_list[node_l].append( [weight,node_r] )
    #adj_list[node_r].append(node_l)
    edges.append([node_l, node_r, weight])

#sort edges:
edges.sort(key=lambda x: x[2])

# disjoin sets:
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]
print(f"parent: {parent}")
print(f"rank: {rank}")
def make_set(i):
    parent[i] = i
    rank[i] = 0

def find(i):
    print(f"i:{i} parent:{parent}")
    while i != parent[i]:
        i = parent[i]
        return i
    
def union(i,j):
    i_id = find(i)
    j_id = find(j)
    if i_id == j_id:
        return 
    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] = rank[j_id]+1


def krusal(adj_list, edges):
    for vertex in range(0,n):
        parent[vertex] = vertex 
        rank[vertex] = 0

    for vertex in range(0,n):
        make_set(vertex)
    
    X = []
    for edge in edges:
        u = edge[0]
        v = edge[1]
        print(f"u:{u} and v:{v}")
        if find(u) != find(v):
            X.append[[u,v]]
            union(u,v)
    return X

