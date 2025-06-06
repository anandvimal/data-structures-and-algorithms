# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        def post(root):
            if root:
                post(root.left)
                post(root.right)
                order.append(root.val)
        post(root)
        return order
        