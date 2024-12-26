import math
import copy
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
    adj_list[node_l].append( [node_r,weight] )
    #adj_list[node_r].append(node_l)

def bellman_ford(adj_list, starting_node):
    for vertex in adj_list:
        distance[vertex] = infinity
        previous[vertex] = None
    distance[starting_node] = 0
    for i in range(0, len(adj_list)-1):
        for vertex in adj_list:
            for edge_and_weight in adj_list[vertex]:
                v = vertex
                u = edge_and_weight[0]
                w = edge_and_weight[1]
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    previous[v] = u

    result = copy.deepcopy(distance)
    for vertex in adj_list:
        for edge_and_weight in adj_list[vertex]:
            v = vertex
            u = edge_and_weight[0]
            w = edge_and_weight[1]
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                previous[v] = u

    if result == distance:
        print("0")
    else:
        print("1")

bellman_ford(adj_list, 1)