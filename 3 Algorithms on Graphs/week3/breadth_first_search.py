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



#fill adj_list with all vertices
for vertex in range(1,n+1):
    adj_list[vertex] = [] 
    #visited[vertex] = False
    #connected_component[vertex] = 0

#populate adj list
for i in range(0,m):
    edge = list(map(int, input().split()))
    node_l = edge[0]
    node_r = edge[1]
    adj_list[node_l].append(node_r)
    adj_list[node_r].append(node_l)

# get the vertix to check for connected component:
starting_node, ending_node =  map(int, input().split())

def bfs(adj_list, starting_node):
    queue = []
    for vertex in adj_list:
        distance[vertex] = infinity
    distance[starting_node] = 0
    queue.append(starting_node)
    while len(queue) != 0:
        u = queue.pop(0) #dequeue function 
        for v in adj_list[u]:
            if distance[v] == infinity:
                queue.append(v)
                distance[v] = distance[u]+1
    
bfs(adj_list, starting_node)

if distance[ending_node] == infinity:
    print("-1")
else:
    print(distance[ending_node])