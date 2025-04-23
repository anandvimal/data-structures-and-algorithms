# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leaf_total = 0

        def leafs(root):
            nonlocal leaf_total
            if not root:
                return 0

            if root.left and not root.left.left and not root.left.right:
                leaf_total += root.left.val

            leafs(root.left)
            leafs(root.right)


        leafs(root)

        return leaf_total 
