import math
infinity = math.inf
#negative_infinity = -math.inf

graph_details = list(map(int, input().split())) 
n = graph_details[0] # total vertices
m = graph_details[1] # total edges

#lets make a adj_list
adj_list = {}

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

# get the vertix to check for connected component:
starting_node, ending_node =  map(int, input().split())

import heapq

# Heap and a mapping for priorities
heap = []
priorities = {}

def add_task(priority, task):
    global heap
    heapq.heappush(heap, (priority, task))
    priorities[task] = priority

def update_priority(new_priority, task ):
    global heap
    if task in priorities:
        del priorities[task]
        heap = [(p, t) for p, t in heap if t != task]
        heapq.heapify(heap)
    add_task(new_priority, task)

def dijkstra(adj_list, starting_node):
    global heap
    for vertex in adj_list:
        distance[vertex] = infinity
        previous[vertex] = None
    distance[starting_node] = 0
    
    for vertex in adj_list:
        add_task(distance[vertex], vertex)
    while len(heap) > 0: 
        u = heapq.heappop(heap)
        u = u[1]
        #print(f"u = {u}")
        for edge in adj_list[u]:
            # print(f"edge: {edge}")
            weight_uv = edge[0]
            v = edge[1]
            # print(f"v:{v}")
            # print(f"u:{u}")
            # print(f"weight_uv:{weight_uv} ")
            # print(f"distance[v]:{distance[v]}")
            # print(f"distance[u]:{distance[u]}")
            if distance[v] > distance[u] + weight_uv:
                distance[v] = distance[u] + weight_uv
                previous[v] = u
                update_priority(distance[v], v)

dijkstra(adj_list, starting_node)
if distance[ending_node] < infinity:
    print(distance[ending_node])
else:
    print("-1")