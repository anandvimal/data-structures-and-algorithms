# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(root):
            queue= [(root,1)]
            
            if not root:
                return 0

            while queue:
                node, depth = queue.pop(0)
                if node.left:
                    queue.append((node.left, depth+1))
                if node.right:
                    queue.append((node.right, depth+1))
                if not node.left and not node.right: # first leaf we encounter
                    return depth

        return depth(root)