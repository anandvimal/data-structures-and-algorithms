import collections

class Node:

    def __init__(self, value, parent, childern = []):
        self.value =value
        self.parent = parent
        self.childern = childern
    
    def add(self, node, target):
        if self.value == target:
            self.childern.append(node)
            return True
        else:
            if len(self.childern) > 0:
                for item in self.childern:
                    item.add(node, target)
                return True
            else:
                return False

    def print_tree(self):
        if self.value is not None:
            print(f"value: {self.value}, parent:{self.parent}")
            pass
        if self.childern != []:
            for item in self.childern:
                item.print_tree()
                            
    def height(self):
        if self.value is not None:
            if self.childern == []:
                return 1
            if len(self.childern) > 0:
                return 1 + max([ item.height() for item in self.childern ])
        else:
            return 0

    def iterative_height(self):
        height = 0 
        queue = collections.deque()

        if self.value == None:
            return height
        
        queue.append(self)

        while queue:
            currSize = len(queue)
            while currSize > 0:
                currNode = queue.popleft()
                currSize -= 1

                if len(currNode.childern) > 0:
                    for item in currNode.childern:
                        queue.append(item)

            height +=1
        return height


if __name__ == "__main__":
    no_of_items = input()
    priority_list = input().strip().split(' ')
    nodes = []
    count = 0

    h = []
    for item in priority_list:
        new_node = Node(value=int(count), parent=int(item), childern=[])
        nodes.append(new_node)
        count=count+1

    r = None
    for xnode in nodes:
        #print(f" {xnode.value} {xnode.parent} {type(xnode.parent)}")
        if xnode.parent == -1:
            r = xnode
            #print("root found")
        else:
            nodes[xnode.parent].childern.append(xnode)

    #print(type(r))
    #r.print_tree()
    #height_of_tree = r.height()
    #print(f"{height_of_tree}")

    height_of_tree_by_iteration = r.iterative_height()
    #print(f"iterative height: {height_of_tree_by_iteration}")

    print(f"{height_of_tree_by_iteration}")
