#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max = -10000
        good_nodes = 0
        
        def findGoodNodes(root, max):
            nonlocal good_nodes
            if root == None : 
                return 0
            elif root.val >= max:
                good_nodes += 1
                max = root.val
            findGoodNodes(root.left, max)
            findGoodNodes(root.right, max)

        findGoodNodes(root, max) 
        return good_nodes           

        