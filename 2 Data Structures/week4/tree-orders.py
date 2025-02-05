# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size



class TreeOrders:
  def read(self):
    self.result = []
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def getLeftChild(self, i):  
    return self.left[i]
    
  def getRightChild(self, i): 
    return self.right[i]
    
  def in_order(self, i):  
    if i == -1:
        return
    self.in_order(self.getLeftChild(i))  
    self.result.append(self.key[i]) 
    self.in_order(self.getRightChild(i))

  def pre_order(self, i):
    if i == -1:
        return
    self.result.append(self.key[i])
    self.pre_order(self.getLeftChild(i))
    self.pre_order(self.getRightChild(i))

  def post_order(self, i):
    if i == -1:
        return
    self.post_order(self.getLeftChild(i))
    self.post_order(self.getRightChild(i))
    self.result.append(self.key[i])

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.in_order(0) 
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.pre_order(0)
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.post_order(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
