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
  if nodes == 0:
    print("CORRECT")
  else:
    IsBinarySearchTree(tree)
    if result == sorted(result):
      print("CORRECT")
    else:
      print("INCORRECT")
    #print(result)
threading.Thread(target=main).start()
#main()