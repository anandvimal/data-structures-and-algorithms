# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:

    def inorder(self, root: Optional[TreeNode]):
        result = []
        def action(root):
            if not root:
                return
            if not root.left  and  not root.right :
                #its a leaf.
                print(root.val)
                result.append(root.val)
            else:              
                action(root.left)
                action(root.right)
        action(root)
        return result

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        result1 = self.inorder(root1)
        
        result2 = self.inorder(root2)

        print(f"result1 {result1}")
        print(f"result2 {result2}")
        if result1 == result2:
            return True
        else:
            return False