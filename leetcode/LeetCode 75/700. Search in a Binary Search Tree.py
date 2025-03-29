# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
#         def search(root, val):
#             if root == None:
#                 return root
#             elif root.val == val:
#                 return root
#             elif root.val > val: 
#                 return search(root.left, val)
#             elif root.val < val:
#                 return search(root.right, val)
        
#         return search(root, val)


# solution 2
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        while root:
            print(root.val)
            if val >  root.val:
                root = root.right
            elif val < root.val:
                root = root.left
            elif root.val == val:
                return root 