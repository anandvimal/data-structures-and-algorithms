parent = []
rank = []

def make_set(i):
    parent[i] = i
    rank[i] = 0

def find(i):
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

    
