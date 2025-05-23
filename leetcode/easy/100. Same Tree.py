# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def same(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val == q.val and same(p.right, q.right)==True and same(p.left,  q.left)==True:
                return True
            else: 
                return False
        return same(p,q)
        

        