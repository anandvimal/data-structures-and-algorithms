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
    
post_order_seq = []
dfs(adj_list)
for i in range(0,len(post)):
    post_order_seq.append(0)

for key in post:
    post_order_seq[post[key]-1]=key

#print(post_order_seq)

reversed_post_order_sequence = ""
for i in range(len(post_order_seq)-1,-1,-1):
    #print(post_order_seq[i])
    reversed_post_order_sequence = reversed_post_order_sequence + str(post_order_seq[i]) + " "

reversed_post_order_sequence = reversed_post_order_sequence.rstrip()
print(reversed_post_order_sequence)
