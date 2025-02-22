#!/usr/bin/python3
import sys, threading
# this works but too slow dont bother with this.

sys.setrecursionlimit(10**7) # max depth of recursion
#https://www.coursera.org/learn/data-structures/discussions/forums/T-oWKMceEeyBoBL7F1DbTw/threads/ggu9m_HYEeyKXA5zGGl7GQ
threading.stack_size(2**27)  # new thread will get stack of such size # 
#result = [] #global variable to store the result of inorder_transversal

# >>> tree[tree[0][1]][0]
# tree[i][1] = 1 #left child
# 1
# >>> tree[tree[0][2]][0]
# tree[i][2] = 2 #right child
# 3

# def inorder_transversal(tree, i):
#   result = []

#   def helper(tree, i):
#     if i == -1:
#         return []
#     helper(tree, tree[i][1])
#     result.append(tree[i][0])
#     helper(tree, tree[i][2])
#     return result

#   helper(tree, i)
  
#   return result

def max_inorder_transversal(tree, i):
  #global result
  result = []
  
  def helper(tree, i):
    nonlocal result
    #global result
    if i == -1:
      return None
    helper(tree, tree[i][1])
    result.append(tree[i][0])
    helper(tree, tree[i][2]) 

  helper(tree, i)
  #print(f"result: {result}")
  return max(result)

def inorder(tree, i):
  voilations = 0

  def helper(tree, i):
    nonlocal voilations
    if i == -1:
      return 0
    else:
      if tree[i][1] != -1:
        # if max_inorder_transversal(tree, tree[i][1]) != None :
          #print(f"max_inorder_transversal(tree,tree[i][1] )  left -> {max_inorder_transversal(tree,tree[i][1] )}")
          #print(f"tree[i][1] -> {tree[i][1]}")
          #print(f"tree[i][0] -> {tree[i][0]}")
          if max_inorder_transversal(tree,tree[i][1] )  >= tree[i][0]: #tree[tree[i][1]][0] # left
            #print("this just happened")
            voilations += 1
          helper(tree, tree[i][1]) #left
      if tree[i][2] != -1 :
        # if max_inorder_transversal(tree, tree[i][2]) != None : 
          #print(f"max_inorder_transversal(tree,tree[i][2] ) right -> {max_inorder_transversal(tree,tree[i][2] )}")
          #print(f"tree[i][0] -> {tree[i][0]}")
          #print(f"tree[i][2] -> {tree[i][2]}")
          if max_inorder_transversal(tree,tree[i][2] )  <= tree[i][0]: # tree[tree[i][2]][0] # right
            #print("this just happened")
            voilations += 1
          helper(tree, tree[i][2]) #right

      

  helper(tree, i)
  return voilations





def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  voilations = inorder(tree, 0)
  #print(f"voilations: {voilations}")
  return voilations

def main():
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
    result =IsBinarySearchTree(tree)
    if result > 0:
      print("INCORRECT")
    else:
      print("CORRECT")
    #print(f"result : {result}")
threading.Thread(target=main).start()
#main()