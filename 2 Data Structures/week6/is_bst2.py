#!/usr/bin/python3
import sys, threading

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

def inorder_transversal(tree, i):
  result = []

  def helper(tree, i):
    if i == -1:
        return []
    helper(tree, tree[i][1])
    result.append(tree[i][0])
    helper(tree, tree[i][2])
    return result

  helper(tree, i)
  
  return result

def check_inorder_transversal(tree, i):
  
  result_left = inorder_transversal(tree, tree[i][1])
  if len(result_left) > 0:
    result_left = max(result_left)  
    if tree[i][0] < result_left:
      return False
  elif len(result_left) == 0:
    return True
  
  result_right = inorder_transversal(tree, tree[i][2])
  if len(result_right) > 0:
    result_right = min(result_right)
    if tree[i][0] > result_right:
      return False
  elif len(result_right) == 0:
    return True
  
  check_inorder_transversal(tree, tree[i][1]) 
  check_inorder_transversal(tree, tree[i][2])
  return True


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  result = check_inorder_transversal(tree, 0)
  return result

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))

  #tree = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]
  #tree = [[1, 1, 2], [2, -1, -1], [3, -1, -1]]
  #tree = [[1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]]
  #tree = [[4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]]
  #tree = [[4, 1, -1], [2, 2, 3], [1, -1, -1], [5, -1, -1]]
  #tree = [[1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]] # 1 -1 1, 2 -1 2, 3 -1 3, 4 -1 4, 5 -1 -1
  print(tree)
  if nodes == 0:
    print("CORRECT")
  else:
    result =IsBinarySearchTree(tree)
    if result == True:
      print("CORRECT")
    else:
      print("INCORRECT")
    #print(f"result : {result}")
threading.Thread(target=main).start()
#main()