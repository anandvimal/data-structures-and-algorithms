#!/usr/bin/python3
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
#https://www.coursera.org/learn/data-structures/discussions/forums/T-oWKMceEeyBoBL7F1DbTw/threads/ggu9m_HYEeyKXA5zGGl7GQ
threading.stack_size(2**27)  # new thread will get stack of such size # 
result_left = [] #global variable to store the result of inorder_transversal
result_right = [] #global variable to store the result of inorder_transversal
tree = []
def inorder_transversal_left(tree, i):
    global result_left
    if i == -1:
        return 
    inorder_transversal_left(tree, tree[i][1])
    result_left.append(tree[i][0])
    #inorder_transversal(tree, tree[i][2]) 

def inorder_transversal_right(tree, i):
    global result_right
    if i == -1:
        return 
    #inorder_transversal_left(tree, tree[i][1])
    result_right.append(tree[i][0])
    inorder_transversal_right(tree, tree[i][2]) 

def IsBinarySearchTree(tree):
  global result_right, result_left
  # Implement correct algorithm here
  inorder_transversal_left(tree, 0)
  inorder_transversal_right(tree, 0)

def check_increasing_order_in_list(list):
  for i in range(1,len(list)):
    if list[i] <= list[i-1]:
      return False
  return True

def main():
  global tree
  global result_left, result_right
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if nodes == 0:
    print("CORRECT")
  else:
    IsBinarySearchTree(tree)
    left = check_increasing_order_in_list(result_left)
    right = result_right == sorted(result_right)
    if left==True and right==True:  
      print("CORRECT")
    else:
      print("INCORRECT")
    #print(result)
    print("result left",result_left)
    print("check left",check_increasing_order_in_list(result_left))
    print("result right",result_right)
#threading.Thread(target=main).start()
#print(check_increasing_order_in_list([2,2]))
main()