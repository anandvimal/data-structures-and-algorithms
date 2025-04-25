# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        data = {}
        def inorder(root):
            nonlocal data
            if root:
                inorder(root.left)
                data[root.val] = data.get(root.val, 0)+1
                inorder(root.right)
        inorder(root)
        #print(data)
        max_value = -1
        for key,value in data.items():
            if value > max_value:
                max_value = value
                max_key = key
        result = []
        for key, value in data.items():
            if value == max_value:
                result.append(key)
        result = list(set(result))
        return result
