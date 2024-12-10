graph_details = list(map(int, input().split())) 
n = graph_details[0] # total vertices
m = graph_details[1] # total edges

#lets make a adj_list
adj_list = {}

#keep tracks for visited nodes
visited = {}
connected_component = {}


#fill adj_list with all vertices
for vertex in range(1,n+1):
    adj_list[vertex] = [] 
    visited[vertex] = False
    #connected_component[vertex] = 0

#populate adj list
for i in range(0,m):
    edge = list(map(int, input().split()))
    node_l = edge[0]
    node_r = edge[1]
    adj_list[node_l].append(node_r)
    adj_list[node_r].append(node_l)


# get the vertix to check for connected component:
vertex_check1, vertex_check2 =  map(int, input().split())


def explore(v, connected_component_counter):
    visited[v] = True
    connected_component[v] = connected_component_counter
    #CCnum(v) = cc
    for vertex in adj_list[v]:
        if not visited[vertex]:
            explore(vertex, connected_component_counter)


def dfs(adj_list):
    for vertex in adj_list:
        visited[vertex] = False
    connected_component_counter = 1
    for vertex in adj_list:
        if not visited[vertex]:
            explore(vertex, connected_component_counter)
            connected_component_counter +=1

 
dfs(adj_list)
if connected_component[vertex_check1] == connected_component[vertex_check2]:
    print("1")
else:
    print("0")


