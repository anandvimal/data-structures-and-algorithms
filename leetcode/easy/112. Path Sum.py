# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathsum(root, targetsum):
            if not root:
                return False
            elif not root.left and not root.right:
                return targetsum - root.val == 0
            else:
                targetsum = targetsum - root.val

                return pathsum(root.left, targetsum) or pathsum(root.right, targetsum)

        return pathsum(root, targetSum)

        