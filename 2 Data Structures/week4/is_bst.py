#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size
#result = [] #global variable to store the result of inorder_transversal
prev = -10000000000 #global variable to store the previous value of the inorder_transversal 


def inorder_transversal(tree, i):
    global prev
    if i == -1:
        return None
    inorder_transversal(tree, tree[i][1])
    if prev < tree[i][0]:
        prev = tree[i][0]
    else:
        return False
    inorder_transversal(tree, tree[i][2]) 

def IsBinarySearchTree(tree):
  global result
  result1 =inorder_transversal(tree, 0)
  # Implement correct algorithm here
  if result1 == False:
    return False
  return True

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if nodes == 0:
    print("CORRECT")
  else:
    if IsBinarySearchTree(tree):
      print("CORRECT")
    else:
      print("INCORRECT")

threading.Thread(target=main).start()
