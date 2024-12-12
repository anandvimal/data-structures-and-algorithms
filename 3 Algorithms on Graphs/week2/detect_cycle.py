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
        if visited[next_vertex] == True:
            is_cycle = True
        visited[next_vertex] = True
        print(f"visited: {next_vertex}")
        if next_vertex not in path:
            path.append(next_vertex)
        print(f"path: {path}")
        print(f"adj_list:{adj_list} has next_vertex:{next_vertex} ?")
        if next_vertex in adj_list: 
            if len(adj_list[next_vertex]) > 0:  #gets next vertex
                next_vertex = adj_list[next_vertex][0] #pick first in list
                print(f"next: {next_vertex}")
            else:
                if next_vertex in path: 
                    path.remove(next_vertex)
                    print(f"removed: {next_vertex}")
                adj_list.pop(next_vertex)
                for key in adj_list:
                    if next_vertex in adj_list[key]:
                        adj_list[key].remove(next_vertex)
                if len(path) > 0:
                    next_vertex = path[-1]
                    visited[next_vertex] = False  #we basically backtracking to previous vertex after finding and removing a sink.
                    print(f"need to revisit : {next_vertex}")
                elif len(adj_list) > 0: #len of path is 0
                    for key in adj_list:
                        if adj_list[key] == []:
                            #adj_list.pop(key)
                            print(f"#1 should removed from adj list  key:{key}  adj_list:{adj_list}")
                        elif len(adj_list[key]) > 0:
                            next_vertex = adj_list[key][0]    
                pass
        else: #adj_list[next_vertex] == [] #sink
            if next_vertex in path: 
                path.remove(next_vertex)
                print(f"removed: {next_vertex}")
            if next_vertex in adj_list:
                adj_list.pop(next_vertex)
            for key in adj_list:
                if next_vertex in adj_list[key]:
                    adj_list[key].remove(next_vertex)
            if len(path) > 0:
                next_vertex = path[-1]
                visited[next_vertex] = False  #we basically backtracking to previous vertex after finding and removing a sink.
                print(f"need to revisit : {next_vertex}")
            elif len(adj_list) > 0: #len of path is 0
                for key in adj_list:
                    if adj_list[key] == []:
                        #adj_list.pop(key)
                        print(f"#2should removed from adj list  key:{key}  adj_list:{adj_list}")
                    elif len(adj_list[key]) > 0:
                        next_vertex = adj_list[key][0]
        print(f"adj_list: {adj_list}")
        print("--")


find_sink_or_cycle(adj_list)
if len(adj_list) > 0:
    print("1") #cycle
else:
    print("0") #linear



