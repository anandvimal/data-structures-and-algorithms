# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        data = []
        def inorder(root):
            nonlocal data
            if root:
                inorder(root.left)
                data.append(root.val)
                inorder(root.right)
            
        inorder(root)
        print(data)
        result = 10000000000000
        for i in range(1, len(data)):
            if result > abs(data[i-1] - data[i]):
                print(data[i-1] - data[i])
                result = abs(data[i-1] - data[i])
        return abs(result)

        