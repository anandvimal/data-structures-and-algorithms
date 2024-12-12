graph_details = list(map(int, input().split())) 
n = graph_details[0] # total vertices
m = graph_details[1] # total edges

#lets make a adj_list
adj_list = {}

#keep tracks for visited nodes
visited = {}
connected_component = {}
post = {}
clock = 1
is_cycle = False

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

def explore(v, connected_component_counter):
    visited[v] = True
    connected_component[v] = connected_component_counter
    for vertex in adj_list[v]:
        if not visited[vertex]:
            explore(vertex, connected_component_counter)
    postvisit(v)

def dfs(adj_list):
    for vertex in adj_list:
        visited[vertex] = False
    connected_component_counter = 1
    for vertex in adj_list:
        if not visited[vertex]:
            explore(vertex, connected_component_counter)
            connected_component_counter +=1

def postvisit(v):
    global clock
    post[v] = clock
    clock = clock+1
    
#return node when its a sink or False if its a cycle
def find_sink_or_cycle(adj_list):
    global is_cycle
    path = []
    next_vertex = next(iter(adj_list)) # start with first
    while is_cycle==False and len(adj_list) > 0:
        while adj_list[next_vertex] != [] and is_cycle==False:
            if next_vertex not in path:
                path.append(next_vertex)
            visited[next_vertex] = True
            next_vertex = adj_list[next_vertex][0]
            #print(f"adj_list:{adj_list} next_vertex:{next_vertex}  adj_list[next_vertex]:{adj_list[next_vertex]}")
            if visited[next_vertex] == True:
                is_cycle = True
        
        if is_cycle ==True:
            break
        # adj_list[next_vertex] = []
        if next_vertex in path:
            path.remove(next_vertex)
        if next_vertex in adj_list:
            adj_list.pop(next_vertex)
        for key in adj_list:
            if next_vertex in adj_list[key]:
                adj_list[key].remove(next_vertex)

        if len(path) > 0:
            next_vertex = path[-1] #backtrack
        elif len(adj_list) > 0:
            next_vertex = next(iter(adj_list)) # start with first again if no path left
        else: #adj_list is empty:   
            #its linear?
            pass
        pass
    pass


find_sink_or_cycle(adj_list)
if len(adj_list) > 0:
    print("1") #cycle
else:
    print("0") #linear



