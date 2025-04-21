# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def t(root):
            if root == None:
                return 
            
            t(root.left)
            result.append(root.val)
            t(root.right)

        t(root)
        print(result)
        return result
        