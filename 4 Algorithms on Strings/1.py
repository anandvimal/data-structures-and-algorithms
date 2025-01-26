#python3
no_of_patterns = int(input())
# patterns = ['ATAGA', 'ATC', 'GAT']
patterns = []
for i in range(no_of_patterns):
    pattern = input()
    patterns.append(pattern)

#print(patterns) 
# of vertices
num_of_vertex = 0
adj_list = {
    0:[],   
}

#print(adj_list)

def lookup_in_adj_list(letter, key):
    for item in adj_list[key]:
        if item[1] == letter:
            return item[0]
    return -1

def trie_construction(patterns):
    global num_of_vertex
    for pattern in patterns:
        lookup_key = 0
        for letter in pattern:
            if lookup_in_adj_list(letter=letter, key=lookup_key) == -1:
                num_of_vertex += 1
                adj_list[lookup_key].append((num_of_vertex, letter))
                adj_list[num_of_vertex] = []
                lookup_key = num_of_vertex
            else:
                lookup_key = lookup_in_adj_list(letter=letter, key=lookup_key)



# def print_adj_list():
#     q = []
#     q.append(0)
#     while len(q) > 0:
#         current = q.pop(0)
#         for item in adj_list[current]:
#             print(f"{current}->{item[0]}:{item[1]}") #coursera does not accept f-string! 
#             q.append(item[0])


def print_adj_list():
    q = [0]
    while q:
        current = q.pop(0)
        for item in adj_list[current]:
            print("{}->{}:{}".format(current, item[0], item[1]))
            q.append(item[0])

trie_construction(patterns) 

print_adj_list()