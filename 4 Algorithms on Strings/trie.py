# text should be appended with atleast one whitespace to work properly for last word to match.

# at end of each pattern should we insert * to know its a leaf node or not?
patterns = ['this', 'that', 'here', 'there', 'alpacas']
text = "this is a wonderful life. my life with pretty alpacas "
class TrieNode():
    def __init__(self):
        self.childern={}

class Trie:
    def __init__(self):
        self.root = TrieNode()

def trie_construction(patterns = patterns):
    trie = Trie() # this contains root only.
    # print(trie)
    # print(trie.root)
    # print(trie.root.childern)
    for pattern in patterns:
        # print(pattern)
        currentNode = trie.root
        # print(currentNode)
        # print(currentNode.childern)

        for alphabet in pattern:
            currentSymbol = alphabet
            if currentSymbol in currentNode.childern :
                currentNode = currentNode.childern[currentSymbol]
            else:
                new_node = TrieNode()
                # add new node from currentNode to newNode with label currentSymbol ???
                currentNode.childern[currentSymbol] = new_node
                currentNode = new_node
                pass
    return trie
    
trie_build = trie_construction(patterns = patterns)

def prefix_trie_matching(text=text, trie=trie_build):
    match = "" #empty string
    text_counter = 0
    symbol = text[text_counter]
    v = trie.root
    while True:
        if v.childern == {}:
            print(f"match: {match}")
            return match
        elif symbol in v.childern :
            match = match + symbol  # constructing the matching word
            v = v.childern[symbol]
            text_counter +=1
            symbol = text[text_counter] #moving to next letter in text
        else:
            print("no outtput found")
            #match = ""
            #v=trie.root
            return
        
def trie_matching(text=text, trie=trie_build):
    text = text + " " # this is needed work last word in the text to match!
    while len(text) > 0:
        prefix_trie_matching(text=text, trie=trie)
        text = text[1:]

trie_matching(text=text, trie=trie_build)