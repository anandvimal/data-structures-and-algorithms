#python3
text = input()
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
            print(f"item[1]: {item[1]}")
            print(f"item[0]: {item[0]} {type(item[0])}")
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


trie_construction(patterns) 

def prefix_trie_matching(text, adj_list):
    match = "" #empty string
    counter = 0
    node_number = 0
    symbol = text[counter]    
    v = adj_list[node_number] # root node
    while True:
        if v == []:
            print(f" match: {match}")
            return match
        elif lookup_in_adj_list(letter=symbol, key = node_number) != -1:
            match = match + symbol
            node_number = lookup_in_adj_list(letter=symbol, key = node_number)
            print(f"node_number: {node_number}")
            v = adj_list[int(node_number)]
            counter += 1
            symbol = text[counter]
        else:
            print("no output found")    
            return  

def trie_matching(text, adj_list):
    text = text + " " # this is needed work last word in the text to match!
    while len(text) > 0:
        prefix_trie_matching(text=text, adj_list=adj_list)
        text = text[1:]

trie_matching(text, adj_list)