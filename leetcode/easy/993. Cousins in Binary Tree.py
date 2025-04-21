# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        result = []
        def dfs(root, parent, depth):
            if root  is None:
                return None
            if root.val ==x or root.val ==y:
                result.append((parent,depth))
            dfs(root.left, root, depth+1)
            dfs(root.right, root, depth+1)
        dfs(root, None, 0)
        x = result[0]
        y = result[1]
        if x[0] != y[0] and x[1] == y[1]:
            return True
        else:
            return False
