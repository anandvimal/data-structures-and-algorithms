#!/usr/bin/python3
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
#https://www.coursera.org/learn/data-structures/discussions/forums/T-oWKMceEeyBoBL7F1DbTw/threads/ggu9m_HYEeyKXA5zGGl7GQ
threading.stack_size(2**27)  # new thread will get stack of such size # 
result = [] #global variable to store the result of inorder_transversal

def inorder_transversal(tree, i):
    global result
    if i == -1:
        return None
    inorder_transversal(tree, tree[i][1])
    result.append(tree[i][0])
    inorder_transversal(tree, tree[i][2]) 

def isBinarySearchTreeProperty(tree, i):
    #global result
    is_search_tree = []  
    def helper(tree, i):
        nonlocal is_search_tree
        if i == -1:
            return None
        current = tree[i][0]
        left = tree[i][1]
        right = tree[i][2]
        if left != -1:
            if tree[left][0] >= current:
                is_search_tree.append(False)
                return None
        if right != -1:
            if tree[right][0] < current:
                is_search_tree.append(False)
                return None
            
        helper(tree, tree[i][1])
        helper(tree, tree[i][2]) 

    helper(tree, i)
    #print(f"result: {result}")
    #print(f"is_search_tree: {is_search_tree}")
    return is_search_tree



def IsBinarySearchTree(tree):
  global result
  # Implement correct algorithm here
  inorder_transversal(tree, 0)


def main():
  global result
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  #nodes =5
  #tree = [[2, 1, 2], [1, -1, -1], [3, -1, -1]] #correct
  #tree = [[1, 1, 2], [2, -1, -1], [3, -1, -1]] #incorrect
  #tree = [[1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]] #correct
  #tree = [[4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]]   #correct  
  #tree = [[4, 1, -1], [2, 2, 3], [1, -1, -1], [5, -1, -1]] #incorrect  
  #tree = [[1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]] # 1 -1 1, 2 -1 2, 3 -1 3, 4 -1 4, 5 -1 -1 #correct
  #print(tree)
  
  if nodes == 0:
    print("CORRECT")
  else:
    IsBinarySearchTree(tree)
    voilations =isBinarySearchTreeProperty(tree, 0)
    #isBinarySearchTree(tree, 0)
    if result == sorted(result) and voilations == []:
      print("CORRECT")
    else:
      print("INCORRECT")
    #print(result)
threading.Thread(target=main).start()
#main()